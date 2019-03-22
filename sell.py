import functools
import uuid
from string import Template

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

bp = Blueprint('marketplace', __name__, url_prefix='/marketplace')

def do_sell_preset(user_id, preset):
    return 0

def store_preset(uuid, user_id, name, meta, binary):
    # store the preset in a database
    get_db().execute(
            'INSERT INTO PRESET VALUES(?,?,?,?)', (uuid,name,meta,binary,)
    )
    get_db().execute(
            'INSERT INTO PRESET_AUTHOR VALUES(?,?)', (uuid,user_id,)
    )
    return

@bp.route('/upload', methods=('POST'))
def upload():
    user = get_logged_in_user()
    if user is None:
        return "false"

    preset_id = uuid.uuid1()
    preset_name = request.form['name']
    preset_metadata = request.form['meta']
    preset_bin = request.form['bin']
    store_preset(preset_id, user.user_id, preset_name, preset_metadata, preset_bin)

    return

def verify_owner(uuid, user_id):
    # TODO
    return True

def sell_preset(uuid):
    # put preset to market place
    get_db().execute(
            'INSERT INTO MARKET_PRESET VALUES(?)', (uuid,)
    )

@bp.route('/sell', methods=('GET', 'POST'))
def sell():
    # to sell a preset, a user should login first
    user = get_logged_in_user()
    if (user is None):
        return "false"

    preset_id = request.form['preset_id']

    if verify_owner(preset_id, user.user_id):
        sell_preset(uuid)
    else:
        return "failed"

    return "success"

