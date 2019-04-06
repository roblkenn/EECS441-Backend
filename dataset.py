import functools
from string import Template
from database.repositories.DatumRepository import DatumRepository
from database.repositories.ImageRepository import ImageRepository
from database.models.Datum import Datum

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, jsonify
)

bp = Blueprint('dataset', __name__, url_prefix='/dataset')

imageRepository = ImageRepository()
datumRepository = DatumRepository()

@bp.route('/', methods=['GET'], strict_slashes=False)
def getDataset():
    json = request.get_json()
    if json is None or 'RowKey' not in json.keys() or json['RowKey'] is None:
        result = datumRepository.read()
        result = [i.__dict__ for i in result]
        return jsonify(result)
    
    return getDatum(json['RowKey'])

def getDatum(RowKey=''):

    try:
        result = datumRepository.read(RowKey=RowKey)
    except:
        return 'Not Found', 404

    result = result.__dict__
    
    return jsonify(result)

@bp.route('/', methods=['POST'], strict_slashes=False)
def postDatum():
    json = request.get_json()

    if not all(k in json.keys() for k in ('imageBase64', 'contrast', 'brightness', 'saturation', 'temperature')):
        return 'Bad Request', 400
        
    try:
        blobName = imageRepository.create(json['imageBase64'])
        json['blobName'] = blobName
    except Exception as e:
        print(e)
        return jsonify({ 'success': False, 'etag': '' })

    try:
        newDatum = Datum(json)
    except Exception as e:
        print(e)
        return 'Bad Request', 400
    
    try:
        etag = datumRepository.create(newDatum)
    except Exception as e:
        print(e)
        return jsonify({ 'success': False, 'etag': '' })

    return jsonify({ 'success': True, 'etag': etag })

@bp.route('/', methods=['DELETE'], strict_slashes=False)
def deleteDatum():
    json = request.get_json()

    try:
        rowKey = json['RowKey']
    except Exception as e:
        print(e)
        return 'Bad Request', 400

    try:
        datumRepository.delete(rowKey)
    except Exception as e:
        print(e)
        return jsonify({ 'success': False })

    return jsonify({ 'success': True })
