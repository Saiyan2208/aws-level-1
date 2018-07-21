def create():
    import boto3
    import sys
    import time
    #name=input('Enter table name to be created: ')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=sys.argv[1],
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
   time.sleep(15)
create()
