import functools
from string import Template
import stripe

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app, jsonify
)

bp = Blueprint('purchase', __name__, url_prefix='/purchase')

stripe.api_key = 'sk_test_vGJklTk0dV19aiOWvP8bk6ik00SDJrMzdh'

@bp.route('', methods=['POST'], strict_slashes=False)
def initiateCharge():
	json = request.get_json()

	userId = json['userId']
	paymentAmount = json['amount']
	tokenId = json['tokenId']

	newCharge = stripe.Charge.create(
		amount=paymentAmount,
		currency='usd',
		source=tokenId,
		description='Test Payment'
	)

	return 'Success', 200
	