import threading
import time

import boto3

from flask import Flask, json

from models.model import init_db, db_session
from models.partner import PartnerJsonSchema, Partner

# Configura el cliente de SQS
sqs = boto3.client('sqs', region_name='us-east-2')
init_db()
partner_schema = PartnerJsonSchema()
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
                    save_partner(message['Body'])
                    # Drop message from queue
                    sqs.delete_message(
                        QueueUrl=queue_url,
                        ReceiptHandle=message['ReceiptHandle']
                    )
            time.sleep(5)


def save_partner(partner_json):
    try:
        partner_dict = json.loads(partner_json)
    except Exception as e:
        print(f"Error al decodificar JSON: {e}")
        return

    partner = Partner(
        name=partner_dict.get('name'),
        description=partner_dict.get('description'),
        price=float(partner_dict.get('price')),
        serviceTypeId=partner_dict.get('serviceTypeId'),
        regionId=partner_dict.get('regionId'),
        countryId=partner_dict.get('countryId'),
        city=partner_dict.get('city'),
        partnerId=partner_dict.get('partnerId')
    )

    db_session.add(partner)
    db_session.commit()


class PartnerService:
    # Start the threat to receive messages
    thread = threading.Thread(target=captured_messages)
    thread.start()
    print('Threat starting to receive messages')
