import json

import boto3

# Create IAM client
iam = boto3.client('iam')

# Create a policy
my_managed_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:864361724244:table/Violations"
        },
        {
            "Effect": "Allow",
            "Action": [
                "rekognition:*"
            ],
            "Resource": "*"
        }
    ]
}
response = iam.create_policy(
  PolicyName='lambdaAccessPolicy',
  PolicyDocument=json.dumps(my_managed_policy)
)

print(response)