import boto3

from flask import Flask, json

# Configura el cliente de SQS
sqs = boto3.client('sqs', region_name='us-east-2')

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
        cola_url = 'https://sqs.us-east-2.amazonaws.com/038172446204/sqssportapp'
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