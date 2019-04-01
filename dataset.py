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

@bp.route('/', methods=['GET'])
def getDataset():
    json = request.get_json()
    if json is None or 'RowKey' not in json.keys() or json['RowKey'] is None:
        result = datumRepository.read()
        return JSONEncoder().encode(result)
    
    return getDatum(json['RowKey'])

def getDatum(RowKey=''):

    result = datumRepository.read(RowKey=RowKey)

    if result is None:
        template = Template('Datum of RowKey "$RowKey" not found')
        return template.substitute(RowKey=RowKey), 404

    print(result)
    
    return JSONEncoder().encode(result)

@bp.route('/', methods=['POST'])
def postDatum():
    json = request.get_json()
    if json is None:
        return 'No JSON', 400
    if 'id' not in json.keys() or json['id'] is None:
        return 'id field is required', 400
    if 'data' not in json.keys() or json['data'] is None:
        return 'data field is required', 400
    
    etag = datumRepository.create(Datum(json))

    return JSONEncoder().encode({ 'etag': etag })

@bp.route('/', methods=['DELETE'])
def deleteDatum():
    json = request.get_json()
    if json is None:
        return 'No JSON', 400
    if 'RowKey' not in json.keys() or json['RowKey'] is None:
        return 'id field is required', 400

    datumRepository.delete(json.RowKey)
    
    return True
