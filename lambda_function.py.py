import boto3

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    print("EVENT:", event)
    try:
        # Get file details from the event
        record = event['Records'][0]
        source_bucket = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']

        destination_bucket = 'destination-victor'  # ✅ Change if needed

        # Copy file
        copy_source = {'Bucket': source_bucket, 'Key': file_key}
        s3_client.copy_object(
            CopySource=copy_source,
            Bucket=destination_bucket,
            Key=file_key
        )

        print(f"✅ Copied '{file_key}' from '{source_bucket}' to '{destination_bucket}'")

        return {
            'statusCode': 200,
            'body': f"File copied successfully: {file_key}"
        }

    except Exception as e:
        print(f"❌ Error copying file: {str(e)}")
        raise
