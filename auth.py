import functools

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
        current_app.logger.info("register: username:%s, password:%s", username, password)
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
