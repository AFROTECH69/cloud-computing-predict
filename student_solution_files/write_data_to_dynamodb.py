import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST data

# Create a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-portfolio-data-table')

def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))

    # Write the data to DynamoDB
    table.put_item(Item={
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message']
    })

    # Create a response object to tell the website that the form data 
    # was successfully received. We use the contents of the decoded JSON dictionary
    # to create this response. As the predict progresses, we'll include 
    # more information about the AWS services we will invoke. 
    lambda_response = {
        'statusCode': 200, # <-- Tells the website that everything executed successfully.
        'body': json.dumps({
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message']
        })
    }

    return lambda_response
