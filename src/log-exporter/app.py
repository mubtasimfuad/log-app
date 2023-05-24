import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        if record['eventName'] == 'REMOVE':
            deleted_item = record['dynamodb']['OldImage']
            
            deleted_item_json = json.dumps(deleted_item)
            
            bucket_name = os.environ['S3BucketName']
            file_key = f'deleted_items/{record["dynamodb"]["Keys"]["id"]["S"]}.json'
            
            s3_client.put_object(
                Body=deleted_item_json,
                Bucket=bucket_name,
                Key=file_key
            )
