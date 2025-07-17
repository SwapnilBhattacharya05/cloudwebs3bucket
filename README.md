# Cloud Backup & Recovery Tool

Python-based backup system that:
- Uploads supported files to AWS S3
- Monitors local changes in real time
- Creates ZIP backups and supports S3 versioning
- Auto-backup every 2 minutes
- Handles file deletion and restores logs

## Technologies Used
- Python
- Boto3 (AWS SDK)
- Watchdog
- AWS S3
