from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
SECRET_KEY='dev',
)

@app.route('/hello', methods=["GET"])
def hello():
	return 'Hello, World!'

import auth
app.register_blueprint(auth.bp)

import dataset
app.register_blueprint(dataset.bp)

import market
app.register_blueprint(market.bp)

import purchase
app.register_blueprint(purchase.bp)

# import machinelearning
# app.register_blueprint(machinelearning.bp)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
