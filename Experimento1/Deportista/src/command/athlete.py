import time
import threading
import boto3

from Experimento1.Deportista.src.models.model import init_db, db_session
from flask import Blueprint

athlete_blueprint = Blueprint('athlete', __name__)
sqs = boto3.client('sqs')

# URL de tu cola de SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/sqssportapp'
init_db()


def captured_messages():
    queue_url = 'https://sqs.us-east-2.amazonaws.com/123456789012/sqssportapp'
    while True:

        try:
            # Recipe the message from queue
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=20
            )
            db_session.add(response)
            db_session.commit()
        except Exception as error:
            print(str(error))
        else:
            if 'Messages' in response:
                for message in response['Messages']:
                    # Process the message received
                    print('Message captured:', message['Body'])
                    # Drop message from queue
                    sqs.delete_message(
                        QueueUrl=queue_url,
                        ReceiptHandle=message['ReceiptHandle']
                    )
            time.sleep(5)


class AthleteService:

    # Start the threat to receive messages
    thread = threading.Thread(target=captured_messages)
    thread.start()
    print('Threat starting to receive messages')