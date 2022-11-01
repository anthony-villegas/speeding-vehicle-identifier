import json
import boto3

# zip this file into a file called lambda.zip then run lambda-deploy.py
# This is the main lambda used to interface from s3 to rekognition



def lambda_handler(event, context):
    rek_client = boto3.client("rekognition", region_name='us-east-1')
    dynamodb_client = boto3.client('dynamodb')
    print(event)

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    image_name = event['Records'][0]['s3']['object']['key']
    time = event['Records'][0]['eventTime']
    print(bucket_name)
    print(image_name)
    print(time)

    response = rek_client.detect_text(
        Image={
            'S3Object': {'Bucket': bucket_name, 'Name':image_name} 
        }
    )
    text = response['TextDetections'][0]['DetectedText']
    print(text)
    
    dynamodb_client.put_item(TableName='Violations', 
        Item={'license_plate':{'S': text}, 'time' : {'S':time}
        })

    return {
        'statusCode': 200,
        'body': json.dumps('License plate detected')
    }