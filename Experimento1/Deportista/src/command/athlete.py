import json
import time
import threading
import boto3

from Experimento1.Deportista.src.models.athlete import Athlete
from Experimento1.Deportista.src.models.model import init_db, db_session
from flask import Blueprint

athlete_blueprint = Blueprint('athlete', __name__)
sqs = boto3.client(
    'sqs',
    region_name='us-east-1',  # o la región que estés utilizando
    endpoint_url='http://localhost:4566',  # URL de LocalStack
)

# URL de tu cola de SQS
init_db()


def captured_messages():
    queue_url = 'https://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/test-queue'
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
