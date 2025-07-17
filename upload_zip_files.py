import boto3
import os

# Setup
bucket_name = '24030142023'
zip_folder = 'C:/Users/Asus/OneDrive/Desktop/SICSR/cloud-backup-tool/zips'
s3_prefix = 'live-sync/backups/'  # Folder in S3

s3 = boto3.client('s3')

# Upload all .zip files
for file_name in os.listdir(zip_folder):
    if file_name.endswith('.zip'):
        local_path = os.path.join(zip_folder, file_name)
        s3_key = s3_prefix + file_name

        try:
            s3.upload_file(local_path, bucket_name, s3_key)
            print(f"✅ Uploaded: {file_name} to S3 → {s3_key}")
        except Exception as e:
            print(f"❌ Failed to upload {file_name}: {e}")
