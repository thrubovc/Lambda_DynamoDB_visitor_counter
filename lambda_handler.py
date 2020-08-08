import boto3
import json
import decimal


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor_counter')


def replace_decimal(obj):
    if isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = replace_decimal(obj[i])
        return obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            obj[k] = replace_decimal(v)
        return obj
    elif isinstance(obj, set):
        return set(replace_decimal(i) for i in obj)
    elif isinstance(obj, decimal.Decimal):
        if obj % 1 == 0:
            return int(obj)
        else:
            return float(obj)
    else:
        return obj


def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'type': 'count'
        },
        UpdateExpression='SET visits = visits + :inc',
        ExpressionAttributeValues={
           ':inc': 1
           },
        ReturnValues='UPDATED_NEW'
    )
    item = response['Attributes']

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(replace_decimal(item))
    }
