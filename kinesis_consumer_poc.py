import boto3
import time

kinesis_stream_name = 'test_stream'

kinesis_client = boto3.client('kinesis', region_name='us-east-1', aws_access_key_id='AKIAWR6VSVBYVBDOPQGN', aws_secret_access_key='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')
response = kinesis_client.describe_stream(StreamName=kinesis_stream_name)
my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(StreamName=kinesis_stream_name,
                                                    ShardId=my_shard_id,
                                                    ShardIteratorType='LATEST')
my_shard_iterator = shard_iterator['ShardIterator']
record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                            Limit=2)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                Limit=2)
    print(record_response,'\n\n')
    time.sleep(5)



# from kinesis.consumer import KinesisConsumer

# boto3_session = boto3.Session(region_name='us-east-1', aws_access_key_id='AKIAWR6VSVBYVBDOPQGN', aws_secret_access_key='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', aws_session_token=boto3.session.Session())

# kinesis_stream_name = 'test_stream'
# consumer = KinesisConsumer(stream_name=kinesis_stream_name, boto3_session=boto3_session)

# for message in consumer:
#     print("Received message: {0}".format(message))
