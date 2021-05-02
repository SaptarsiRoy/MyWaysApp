import json
import boto3


def lambda_handler(event, context):
    parameter = event['queryStringParameters']
    
    database = boto3.resource('dynamodb')
    table = database.Table('My_Ways')
    
    rp = table.get_item(Key={
        'id': parameter["id"]
        }
    )
    if 'Item' not in rp:
        x = "Candidate Not Present"
        
    else:
        rp1 = table.delete_item(Key={
               'id': parameter['id']
               }
            )
        if rp1['ResponseMetadata']['HTTPStatusCode'] == 200:
                x = "Candidate Deleted Successfully"
    return {
        'statusCode': 200,
        'body': json.dumps(x)
    }
