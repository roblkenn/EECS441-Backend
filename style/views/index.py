"""
style main view

"""
import os
import flask
import style

@style.app.route('/', methods=["GET"])
def show_index():
    """Display / route."""
    # if 'username' not in flask.session:
    #     return flask.redirect('/accounts/login/')
    return json.dumps({'data':'Hello World'})