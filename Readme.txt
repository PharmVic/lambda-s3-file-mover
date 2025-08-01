# AWS Lambda + S3: File Mover

This project demonstrates how to use AWS Lambda to automatically copy a file from one S3 bucket to another when a new file is uploaded.

## 🔧 How It Works

- The Lambda function is triggered by an **S3 upload event**.
- It reads the event to determine the source bucket and file name.
- It copies the uploaded file to a **destination bucket**.

## 📁 Project Structure

