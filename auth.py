import functools
import uuid
import hashlib

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
    current_app
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    # placeholder
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        salt = uuid.uuid4().hex
        hash_obj = hashlib.new('sha512')
        password_salted = salt + password
        hash_obj.update(password_salted.encode('utf-8'))

        # Save POST request's file object to a temp file
        dummy, temp_filename = tempfile.mkstemp()
        file.save(temp_filename)
        # Compute filename
        hash_txt = sha256sum(temp_filename)
        dummy, suffix = os.path.splitext(file.filename)
        hash_password = hash_txt + suffix

        current_app.logger.info("register: username:%s, password:%s", username, hash_password)
        return "success"
    else:
        return "failed"


@bp.route('/login', methods=('GET', 'POST'))
def login():
    # placeholder
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        current_app.logger.info("login: username:%s, password:%s", username, password)


        # extract the salt
        salt = password_db[password_db.find('$') + 1: password_db.rfind('$')]
        hash_obj = hashlib.new(algorithm)
        password_salted = salt + password
        hash_obj.update(password_salted.encode('utf-8'))
        password_hash = hash_obj.hexdigest()
        password_db_string = "$".join([algorithm, salt, password_hash])

        # if password_db_string == password_db:
            # return success
        if (username == "123" and password == "234"):
            session.clear()
            session['user_id'] = "123"
            return "success"
        else:
            return "failed"
    else:
        return "failed"


@bp.route('/logout')
def logout():
    # placeholder
    session.clear()
    return "success"


@bp.before_app_request
def get_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
		# get real user data from the database
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

    return g.user
