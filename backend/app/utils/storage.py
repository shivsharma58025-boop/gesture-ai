from minio import Minio
import os


def get_minio_client():
    endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")
    access = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
    secret = os.getenv("MINIO_SECRET_KEY", "minioadmin")
    return Minio(endpoint, access_key=access, secret_key=secret, secure=False)


def upload_clip(bucket: str, object_name: str, file_path: str):
    client = get_minio_client()
    if not client.bucket_exists(bucket):
        client.make_bucket(bucket)
    client.fput_object(bucket, object_name, file_path)
