import boto3

lambda_client = boto3.client('lambda')
client = boto3.client("s3")

response1 = lambda_client.add_permission(FunctionName='arn:aws:lambda:us-east-1:864361724244:function:s3ReactionLambda',
                               StatementId='response2-id-2',
                               Action='lambda:InvokeFunction',
                               Principal='s3.amazonaws.com',
                               SourceArn='arn:aws:s3:::license-plate-images-bucket'
                              )
response2 = lambda_client.get_policy(FunctionName='arn:aws:lambda:us-east-1:864361724244:function:s3ReactionLambda')


#setting s3 to trigger lambda
response = client.put_bucket_notification_configuration(
                            Bucket='license-plate-images-bucket',
                            NotificationConfiguration= {'LambdaFunctionConfigurations':[{'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:864361724244:function:s3ReactionLambda', 'Events': ['s3:ObjectCreated:*']}]})