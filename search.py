'''
Searches for an item in the dynamodb endpoint url given
Used in Lambda function with read permission from dynamodb
'''


import cgi
import boto3
from botocore.exceptions import ClientError


def search():
    form = cgi.FieldStorage()
    candidate_key = int(form.getvalue("ckey"))

    database = boto3.resource('dynamodb', endpoint_url="")

    table = database.Table('MyWays')

    try:
        response = table.get_item(Key={'ckey': candidate_key})
    except ClientError as e:
        response = "NO client key available"

    return response['item']
