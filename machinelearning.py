import functools
import uuid
from string import Template
from database.repositories.ListingRepository import ListingRepository
from database.repositories.UserRepository import UserRepository
from database.models.Listing import Listing
from database.models.User import User
from transferlearning import run_user_model, train_user_model

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, jsonify
)

bp = Blueprint('ml', __name__, url_prefix='/ml')

@bp.route('', methods=['GET'], strict_slashes=False)
def editPhoto():
	json = request.get_json()

	if 'userId' not in json.keys():
		return 'Bad Request', 400

	if 'modelId' not in json.keys():
		return 'Bad Request', 400

	if 'imageBase64' not in json.keys():
		return 'Bad Request', 400

	result = run_user_model(json['modelId'], json['imageBase64'])

	return jsonify(result)

@bp.route('', methods=['POST'], strict_slashes=False)
def trainModel():
	json = request.get_json()

	if 'userId' not in json.keys():
		return 'Bad Request', 400
	
	if 'modelId' not in json.keys():
		return 'Bad Request', 400

	if 'imageBase64' not in json.keys():
		return 'Bad Request', 400

	if json['modelId'] != json['userId']:
		return 'Done', 200

	train_user_model(json['userId'], json['imageBase64'], json['contrast'], json['brightness'], json['temperature'], json['saturation'])

	return 'Done', 200