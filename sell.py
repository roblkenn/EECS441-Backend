import functools
import uuid
from string import Template

from flask import (
        Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

bp = Blueprint('marketplace', __name__, url_prefix='/marketplace')

# api section
def post_preset(uid, user_id, name, price):
    # sell preset
    get_db().execute(
            'INSERT INTO MARKET VALUES(?,?,?,?,?)', (uid, user_id, name, price,)
    )
    return 0

def store_preset(uid, user_id, name, meta, binary):
    # store the preset in a database
    # FIXME! how to present preset data
    get_db().execute(
            'INSERT INTO PRESET VALUES(?,?,?,?)', (uid,name,meta,binary,)
    )
    get_db().execute(
            'INSERT INTO PRESET_AUTHOR VALUES(?,?)', (uuid,user_id,)
    )
    return

def verify_owner(uid, user_id):
    # verify owner
    get_db().execute(
        "SELECT * FROM PRESET_AUTHOR WHERE uid=?", (uid,)
    )
    fetch_id = get_db().fetchall()[0]
    if user_id == fetch_id:
        return True
    return False

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

