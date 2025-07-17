import boto3

bucket_name = '24030142023'
s3_key = 'live-sync/backups/images.zip'

s3 = boto3.client('s3')

response = s3.list_object_versions(Bucket=bucket_name, Prefix=s3_key)

versions = response.get('Versions', [])
if not versions:
    print("❌ No versions found.")
else:
    print(f"🗂️ Found {len(versions)} version(s) of: {s3_key}")
    for v in versions:
        print(f" - VersionId: {v['VersionId']} | LastModified: {v['LastModified']} | Size: {v['Size']} bytes")
