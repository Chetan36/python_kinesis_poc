import boto3
import json
from datetime import datetime
import calendar
import random
import time

kinesis_stream_name = 'test_stream'

kinesis_client = boto3.client('kinesis', region_name='us-east-1', aws_access_key_id='AKIAWR6VSVBYVBDOPQGN', aws_secret_access_key='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')

def push_data_to_stream(status, message, data, property_timestamp):
    payload = {
                'status': status,
                'message': message,
                'data': data
              }

    print(payload)

    put_response = kinesis_client.put_record(
                        StreamName=kinesis_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=str(property_timestamp))

while True:
    status = random.randint(200, 500)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    message = 'Hello there, you just put me in the stream'
    data = { 'name': 'Priyabrata Pati', 'age': 25, 'designation': 'Sr. Software Engineer' }

    push_data_to_stream(status, message, data, property_timestamp)

    # wait for 5 second
    time.sleep(5)
