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

@insta485.app.route('/uploads/<path:filename>')
def send_file(filename):
    """Send file."""
    return flask.send_from_directory(
        style.app.config['UPLOAD_FOLDER'],
        filename, as_attachment=True
    )

@style.app.route()
def sign_up():

