import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Violations',
    KeySchema=[
        {
            'AttributeName': 'license_plate',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'time',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'license_plate',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'time',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)