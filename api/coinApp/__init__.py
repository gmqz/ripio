# App __init__
from flask import Flask
from flask_restful import Api
from mongoengine import *

app = Flask(__name__)
#Load config to flask instance
app.config.from_pyfile('config.py')

#Connect to PyMongo(app)
mongo = connect('ripio', host='mongo')

#Instance of flask_restful
api = Api(app, prefix="/api")

def errorHandler(   code = 404,
                    debug = "",
                    message = "Unfortunately something went wrong."):
    response = {
                'status': 'Fail',
                'message': message,
            }

    if app.config['DEBUG'] :
        response['debug'] = str(debug)

    return response, code

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response
