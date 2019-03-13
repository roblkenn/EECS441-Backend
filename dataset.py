import functools
from string import Template

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    current_app
)

bp = Blueprint('dataset', __name__, url_prefix='/dataset')

@bp.route('/', methods=['GET'])
def getDataset():
    json = request.get_json()
    if json is None or 'id' not in json.keys() or json['id'] is None:
        return '[ { "id": "0", "data": "*data0" }, { "id": "1", "data": "*data1" }, { "id": "2", "data": "*data2" } ]'
    
    return getDatum(json['id'])

def getDatum(id=''):
    if id == 'error':
        template = Template('Datum of id "$id" not found')
        return template.substitute(id=id), 404
    else:
        template = Template('{ "id": $id, "data": "*data*" }')
        return template.substitute(id=id)

@bp.route('/', methods=['POST'])
def postDatum():
    json = request.get_json()
    if json is None:
        return 'No JSON', 400
    if 'id' not in json.keys() or json['id'] is None:
        return 'id field is required', 400
    if 'data' not in json.keys() or json['data'] is None:
        return 'data field is required', 400

    template = Template('{ "id": "$id" "data": "$data" }')
    return template.substitute(id=json['id'], data=json['data'])

@bp.route('/', methods=['DELETE'])
def deleteDatum():
    json = request.get_json()
    if json is None:
        return 'No JSON', 400
    if 'id' not in json.keys() or json['id'] is None:
        return 'id field is required', 400

    template = Template('{ "succeeded": true, "message": "datum {id} remove from dataset" }')
    return template.substitute(id=id)
