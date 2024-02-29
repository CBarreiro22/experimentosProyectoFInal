import os
from flask import Flask, jsonify
from Experimento1.Usuario.src.blueprints.operation import operations_blueprint
from Experimento1.Usuario.src.errors.errors import ApiError


app = Flask(__name__)
app.register_blueprint(operations_blueprint)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "mssg": err.description,
        "version": os.environ["VERSION"]
    }
    return jsonify(response), err.code