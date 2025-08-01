# Lambda S3 File Mover

This AWS Lambda function automatically copies files from one S3 bucket to another when a new file is uploaded.

## How It Works

- Trigger: S3 Event (ObjectCreated:Put)
- Source Bucket: `sourcebucket2002`
- Destination Bucket: `targetbucket2002`
- Language: Python 3.13
- AWS Services: Lambda, S3, IAM

## Files

- `lambda_function.py`: Your Lambda function code
- `role-policy.json`: IAM role policy allowing Lambda access to S3

## Setup

1. Create two S3 buckets: source and destination.
2. Create IAM Role with the trust and permission policy in `role-policy.json`.
3. Deploy the Lambda and connect it to your source bucket using an S3 trigger.
