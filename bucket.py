import boto3

s3 = boto3.client('s3')

bucket_name = '24030142023'

# Create bucket
s3.create_bucket(Bucket=bucket_name)
print(f"Bucket '{bucket_name}' created.")
