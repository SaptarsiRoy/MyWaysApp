import json
import boto3


def lambda_handler(event, context):
    parameter = event['queryStringParameters']

    database = boto3.resource('dynamodb')
    table = database.Table('MyWays')
    rp = table.get_item(Key={
        'id': parameter["id"]
        }
    )
    if 'Item' not in rp:
        rp1 = table.put_item(
            Item={
                'id': parameter['id'],
                'Name': parameter['name'],
            }
        )
        if rp1['ResponseMetadata']['HTTPStatusCode'] == 200:
            x = "Candidate Created Successfully"
    else:
        x = "Already Present"

    return {
        'statusCode': 200,
        'body': json.dumps(x)
    }
