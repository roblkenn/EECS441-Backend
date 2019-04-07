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

# @bp.route('updateListing', methods=['POST'], strict_slashes=False)
# def updateListing():
#     json = request.get_json()

#     try:
#         user = User(json)
#     except Exception as e:
#         print(e)
#         return 'Bad Request', 400

#     try:
#         user = userRepository.read(RowKey=user.RowKey)
#     except Exception as e:
#         return 'Bad Request', 400

#     try:
#         newListing = Listing(json)
#     except Exception as e:
#         print(e)
#         return 'Bad Request', 400
    
#     try:
#         if (getListing(newListing.RowKey)):
#             print("already exist, update lisging")
#             etag = listingRepository.updateListing(newListing)
#         else:
#             return 'Bad Request', 400
#     except Exception as e:
#         print(e)
#         return 'Bad Request', 500

#     return jsonify({ 'success': True, 'etag': etag })

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
