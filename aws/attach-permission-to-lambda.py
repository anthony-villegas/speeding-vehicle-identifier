import boto3
iam = boto3.client('iam')

iam.attach_role_policy(
    PolicyArn='arn:aws:iam::864361724244:policy/lambdaAccessPolicy',
    RoleName='LambdaBasicExecution'
)

