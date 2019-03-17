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

@style.app.route('/signup', methods=['GET', 'POST'])
def sign_up():

if flask.request.method == "POST":

        # get user name and password from form
        # password = 
        # fullname = 
        # file = 

        # otherwise salt and hash inputted password
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
        hash_filename_basename = hash_txt + suffix
        hash_filename = os.path.join(
            style.app.config["UPLOAD_FOLDER"],
            hash_filename_basename
        )

        # Move temp file to permanent location
        shutil.move(temp_filename, hash_filename)
        style.app.logger.debug("Saved %s", hash_filename_basename)

        # update database

        flask.session["username"] = username
        return flask.redirect('/')

    else:
        return flask.redirect('/')