import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from commands.partner_service import PartnerService

loaded = load_dotenv('.env.development')

app = Flask(__name__)


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
