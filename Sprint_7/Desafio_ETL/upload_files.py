import os
from pathlib import Path
from glob import glob
import boto3
from datetime import datetime


s3 = boto3.client(
    's3',
    aws_access_key_id="",
    aws_secret_access_key="f",
    aws_session_token="")

path1 = os.getcwd()
csv_files = glob(os.path.join(path1, "*.csv"))

AWS_REGION = "us-east-1"
S3_BUCKET_NAME = "aylu-compasso"

now = datetime.now()
datenow = now.strftime("%Y/%m/%d")



def upload_file(file_name, bucket, object_name):
    if object_name is None:
        object_name = file_name
    s3.upload_file(file_name, bucket, object_name)

for file in csv_files:
    namefile = (Path(file).stem)
    upload_file(file, S3_BUCKET_NAME, 'Raw/Local/CSV/{}/{}/{}'.format(namefile, datenow, namefile))

