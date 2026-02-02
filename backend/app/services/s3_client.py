import boto3
import os
import uuid

# Create S3 client using env vars
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)

BUCKET = os.getenv("S3_BUCKET")


def upload_menu_file(file_bytes: bytes, filename: str) -> str:
    ext = filename.split(".")[-1]
    key = f"menus/{uuid.uuid4()}.{ext}"

    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=file_bytes,
        ContentType="application/octet-stream",
    )

    return f"s3://{BUCKET}/{key}"
