import functools
import uuid
from string import Template
from database.repositories.ListingRepository import ListingRepository
from database.repositories.UserRepository import UserRepository
from database.models.Listing import Listing
from database.models.User import User

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, jsonify
)

bp = Blueprint('market', __name__, url_prefix='/market')

listingRepository = ListingRepository()
userRepository = UserRepository()

# # api section
# def post_preset(uid, user_id, name, price):
#     # sell preset
#     get_db().execute(
#             'INSERT INTO MARKET VALUES(?,?,?,?,?)', (uid, user_id, name, price,)
#     )
#     return 0

# def store_preset(uid, user_id, name, meta, binary):
#     # store the preset in a database
#     # FIXME! how to present preset data
#     get_db().execute(
#             'INSERT INTO PRESET VALUES(?,?,?,?)', (uid,name,meta,binary,)
#     )
#     get_db().execute(
#             'INSERT INTO PRESET_AUTHOR VALUES(?,?)', (uuid,user_id,)
#     )
#     return

# def verify_owner(uid, user_id):
#     # verify owner
#     get_db().execute(
#         "SELECT * FROM PRESET_AUTHOR WHERE uid=?", (uid,)
#     )
#     fetch_id = get_db().fetchall()[0]
#     if user_id == fetch_id:
#         return True
#     return False

# @bp.route('', methods=('POST'))
# def upload():
#     user = get_logged_in_user()
#     if user is None:
#         return "false"

#     preset_id = uuid.uuid1()
#     preset_name = request.form['name']
#     preset_metadata = request.form['meta']
#     preset_bin = request.form['bin']
#     store_preset(preset_id, user.user_id, preset_name, preset_metadata, preset_bin)

#     return

# @bp.route('', methods=('GET', 'POST'))
# def sell():
#     # to sell a preset, a user should login first
#     user = get_logged_in_user()
#     if (user is None):
#         return "false"

#     preset_id = request.form['preset_id']

#     if verify_owner(preset_id, user.user_id):
#         sell_preset(uuid)
#     else:
#         return "failed"

#     return "success"

@bp.route('', methods=['GET'], strict_slashes=False)
def getAllListings():
    json = request.get_json()
    
    if json is None or 'RowKey' not in json.keys() or json['RowKey'] is None:
        result = listingRepository.read()
        result = [i.__dict__ for i in result]
        return jsonify(result)
    
    return getListing(json['RowKey'])

def getListing(RowKey):
    try:
        result = listingRepository.read(RowKey=RowKey)
    except Exception as e:
        print(e)
        return 'Not Found', 404

    result = result.__dict__
    
    return jsonify(result)

@bp.route('', methods=['POST'], strict_slashes=False)
def createListing():
    json = request.get_json()

    try:
        user = User(json)
    except Exception as e:
        print(e)
        return 'Bad Request', 400

    try:
        user = userRepository.read(RowKey=user.RowKey)
    except Exception as e:
        print('Creating new user')
        userRepository.create(user)

    try:
        newListing = Listing(json)
    except Exception as e:
        print(e)
        return 'Bad Request', 400
    
    try:
        etag = listingRepository.create(newListing)
    except Exception as e:
        print(e)
        return jsonify({ 'success': False, 'etag': '' })

    return jsonify({ 'success': True, 'etag': etag })

@bp.route('', methods=['DELETE'], strict_slashes=False)
def deleteListing():
    json = request.get_json()

    try:
        rowKey = json['RowKey']
    except Exception as e:
        print(e)
        return 'Bad Request', 400

    try:
        listingRepository.delete(rowKey)
    except Exception as e:
        print(e)
        return jsonify({ 'success': False })

    return jsonify({ 'success': True })