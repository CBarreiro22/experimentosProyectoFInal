import json
import os
import time
import threading
import boto3

from ..models.model import init_db, db_session
from flask import Blueprint
from ..models.athlete import Athlete

athlete_blueprint = Blueprint('athlete', __name__)
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"]
)

# URL de tu cola de SQS
init_db()


def captured_messages():
    queue_url = 'https://sqs.us-east-1.amazonaws.com/914985899514/user-experimento.fifo'
    while True:

        try:
            # Recipe the message from queue
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=20
            )
            # db_session.add(response)
            # db_session.commit()
        except Exception as error:
            print(str(error))
        else:
            if 'Messages' in response:
                for message in response['Messages']:
                    # Process the message received
                    print('Message captured:', message['Body'])
                    athlete_data = parse_message(message)  # Suponiendo que tienes una función para parsear el mensaje
                    athlete = Athlete(**athlete_data)
                    db_session.add(athlete)
                    db_session.commit()
                    # Drop message from queue
                    sqs.delete_message(
                        QueueUrl=queue_url,
                        ReceiptHandle=message['ReceiptHandle']
                    )
            time.sleep(5)


def parse_message(message):
    # Suponiendo que el mensaje está en formato JSON y tiene campos que corresponden a los atributos de Athlete
    try:
        print('este esw un message', message)
        print('typeof', type(message['Body']))
        athlete_data = json.loads(message['Body'])
        return athlete_data
    except json.JSONDecodeError:
        print("Error: El mensaje no está en formato JSON válido.")
        return None


class AthleteService:
    # Start the threat to receive messages
    thread = threading.Thread(target=captured_messages)
    thread.start()
    print('Threat starting to receive messages')


@athlete_blueprint.route('/deportista/health', methods=['GET'])
def check_health():
    return 'ok', 200
