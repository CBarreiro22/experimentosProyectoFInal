import os
import uuid

import boto3

from flask import Flask, json

# Configura el cliente de SQS
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"]
)


class Athlete:

    @staticmethod
    def create_athlete(body):
        print(body)
        response = Athlete.send_message_topic(body)
        if response[1] == 201:
            return "", ""
        else:
            return response[0], response[1]

    @staticmethod
    def send_message_topic(message):
        cola_url = 'https://sqs.us-east-1.amazonaws.com/914985899514/user-experimento.fifo'
        message_json = json.dumps(message)
        print(message_json)
        try:
            # Envía el mensaje a la cola de SQS
            sqs.send_message(
                QueueUrl=cola_url,
                MessageBody=message_json,
                MessageGroupId='user',
                MessageDeduplicationId=str(uuid.uuid4())
            )
        except Exception as error:
            return str(error), 500
        else:
            return '', 200
