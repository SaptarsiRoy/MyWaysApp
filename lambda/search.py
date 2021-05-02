import boto3
import json

def lambda_handler(event, context):
    parameter = event['queryStringParameters']
    
    database = boto3.resource('dynamodb')
    table = database.Table('My_Ways')
    rp = table.get_item(Key={
        'id': parameter["id"]
        }
    )
    
    if 'Item' not in rp:
        x = "No valid Key present"
    else:
        x = rp['Item']['id'] + "\n" + rp['Item']['Name']
    
    return {
        'statusCode': 200,
        'body': json.dumps(x)
    }