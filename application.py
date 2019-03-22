import os
from flask import Flask

# Use the code below to access environment variables
# os.environ['WEBSITE_SITE_NAME']

app = Flask(__name__)
app.config.from_mapping(
SECRET_KEY='dev',
)

@app.route('/hello')
def hello():
	return 'Hello, World!'

import auth
app.register_blueprint(auth.bp)

import dataset
app.register_blueprint(dataset.bp);

if __name__ == "__main__":
	app.run(host='0.0.0.0')
