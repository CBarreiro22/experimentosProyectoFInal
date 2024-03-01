import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from .commands.partner_service import PartnerService
from .blueprints.operations import operations_blueprint

loaded = load_dotenv('.env.development')

app = Flask(__name__)
app.register_blueprint(operations_blueprint)


def start_consumer():
    PartnerService()

if __name__ == '__main__':
    start_consumer()

def handle_exception(err):
    response = {
        "msg": err.description,
        "version": os.environ["VERSION"]
    }
    return jsonify(response), Exception(err.code)
