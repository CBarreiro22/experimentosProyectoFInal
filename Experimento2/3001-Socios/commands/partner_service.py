import threading
import time

import boto3

from flask import Flask

# Configura el cliente de SQS
sqs = boto3.client('sqs', region_name='us-east-2')

app = Flask(__name__)


def captured_messages():
    queue_url = 'https://sqs.us-east-2.amazonaws.com/038172446204/sqssportapp'
    while True:

        try:
            # Recipe the message from queue
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=20
            )
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


class PartnerService:

    # Start the threat to receive messages
    thread = threading.Thread(target=captured_messages)
    thread.start()
    print('Threat starting to receive messages')
