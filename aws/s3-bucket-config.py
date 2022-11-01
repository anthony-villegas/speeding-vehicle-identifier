import boto3

# if region not specified uses us-east-1 by default
client = boto3.client("s3")

bucket_name = "license-plate-images-bucket"
client.create_bucket(Bucket=bucket_name)

print("Amazon S3 bucket has been created")