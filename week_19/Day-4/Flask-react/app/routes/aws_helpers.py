import boto3
import botocore
import os
import uuid 

BUCKET_NAME=os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET"),
)


def get_unique_filename(filename):
    ext = filename.split('.', 1)[1].lower()
    unique_filename = uuid.uuid4().hex
    return f"{unique_filename}.{ext}"


def upload_file_to_s3(file, acl="public-read"):
    try:
        s3.upload_fileobj(
            file, 
            BUCKET_NAME,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        return {"errors": str(e)}


    return {'url': f"{S3_LOCATION}{file.filename}"}


