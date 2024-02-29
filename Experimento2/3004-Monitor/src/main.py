import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from .blueprints.operations import operations_blueprint
from .error.errors import ApiError

loaded=load_dotenv('.env.development')

app = Flask(__name__)
app.register_blueprint(operations_blueprint)

@app.errorhandler(ApiError)
def handle_api_error(error):
    if error.description == '':
        return error.description, error.code
    return jsonify({
        "mssg": error.description,
        "version": os.environ["VERSION"]
    }), error.code