import boto3

from flask import Flask, json

# Configura el cliente de SQS
sqs = boto3.client('sqs', region_name='us-east-2')


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
        cola_url = 'https://sqs.us-east-2.amazonaws.com/123456789012/sqssportapp'
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
