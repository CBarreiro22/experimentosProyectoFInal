import os

import boto3
from dotenv import load_dotenv

from flask import Flask, json

loaded = load_dotenv('.env.development')

# Configura el cliente de SQS
sqs = boto3.client(
    'sqs',
    region_name='us-east-2',
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"]
)

app = Flask(__name__)

class PartnerService:

    @staticmethod
    def create_partner_service(body):
        response = PartnerService.send_message_topic(body)
        if response[1] == 201:
            return "", ""
        else:
            return response[0], response[1]

    @staticmethod
    def send_message_topic(message):
        # Se asume que 'request' está disponible, si no, debes proporcionar el contexto adecuado
        cola_url = 'https://sqs.us-east-1.amazonaws.com/914985899514/user-experimento.fifo'
        message_json = json.dumps(message)
        try:
            # Envía el mensaje a la cola de SQS
            response = sqs.send_message(
                QueueUrl=cola_url,
                MessageBody=message_json
            )
        except Exception as error:
            return str(error), 500
        else:
            return '', 200