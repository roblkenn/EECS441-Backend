"""style configuration."""

import os

APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'd\x89\x05\xc9\xa6X\xd9lc\xa9k\x9c\xaf5~y\x08\x82\xa0\x95\xfd\x12!F'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jepg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is ...
#DATABASE_FILENAME = os.path.join()
