"""
style package initializer.

"""
import flask

app = flask.Flask(__name__)

app.config.from_object('style.config')

import style.api   
import style.views 
