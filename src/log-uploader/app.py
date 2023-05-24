import json
import boto3
import time
from datetime import datetime, timedelta

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('log-table')

    print(str(event))

    expiration_time = int(time.time()) + 300

    log_entry = {
        'id': str(int(time.time())),
        'log': event,
        'expirationTime': expiration_time
    }

    table.put_item(Item=log_entry)
    response = table.scan()
    print(response['Items'][0])

    return {
        'statusCode': 200,
        'body': "Uploaded to dynamodb"
            
        
    }
