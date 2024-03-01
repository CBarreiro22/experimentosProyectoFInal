import boto3

from flask import Flask, json

# Configura el cliente de SQS
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',  # o la región que estés utilizando
    endpoint_url='http://localhost:4566',  # URL de LocalStack
)


class Athlete:

    @staticmethod
    def create_athlete(body):
        response = Athlete.send_message_topic(body)
        if response[1] == 201:
            return "", ""
        else:
            return response[0], response[1]

    @staticmethod
    def send_message_topic(message):
        cola_url = 'http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/test-queue'
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
