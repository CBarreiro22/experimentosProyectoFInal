from flask import Flask, jsonify
from dotenv import load_dotenv
from .command.athlete import athlete_blueprint
from .errors.errors import ApiError

app = Flask(__name__)
app.register_blueprint(athlete_blueprint)

loaded = load_dotenv('.env.development')


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "mssg": err.description,
        "version": "1.0"
    }
    return jsonify(response), err.code
