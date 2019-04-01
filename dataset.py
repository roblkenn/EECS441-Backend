import functools
from string import Template
from database.repositories.DatumRepository import DatumRepository
from database.models.Datum import Datum
from json import JSONEncoder, JSONDecoder

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    current_app
)

bp = Blueprint('dataset', __name__, url_prefix='/dataset')

datumRepository = DatumRepository()

@bp.route('/', methods=['GET'], strict_slashes=False)
def getDataset():
    json = request.get_json()
    if json is None or 'RowKey' not in json.keys() or json['RowKey'] is None:
        result = datumRepository.read()
        result = [i.__dict__ for i in result]
        return JSONEncoder().encode(result)
    
    return getDatum(json['RowKey'])

def getDatum(RowKey=''):

    try:
        result = datumRepository.read(RowKey=RowKey)
    except:
        return 'Not Found', 404

    if result is None:
        template = Template('Datum of RowKey "$RowKey" not found')
        return template.substitute(RowKey=RowKey), 404

    result = result.__dict__
    
    return JSONEncoder().encode(result)

@bp.route('/', methods=['POST'], strict_slashes=False)
def postDatum():
    json = request.get_json()

    try:
        newDatum = Datum(json)
    except Exception as e:
        print(e)
        return 'Bad Request', 400
    
    try:
        etag = datumRepository.create(newDatum)
    except Exception as e:
        print(e)
        return JSONEncoder().encode({ 'success': False, 'etag': '' })

    return JSONEncoder().encode({ 'success': True, 'etag': etag })

@bp.route('/', methods=['DELETE'], strict_slashes=False)
def deleteDatum():
    json = request.get_json()

    try:
        rowKey = json.RowKey
    except:
        return 'Bad Request', 400

    try:
        datumRepository.delete(rowKey)
    except:
        return JSONEncoder().encode({ 'success': False })

    return JSONEncoder().encode({ 'success': True })
