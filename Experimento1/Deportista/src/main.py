from flask import Flask, jsonify

from .blueprints.athlete import athlete_blueprint
from .errors.errors import ApiError
app = Flask(__name__)
app.register_blueprint(athlete_blueprint)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description,
      "version": "1.0"
    }
    return jsonify(response), err.code