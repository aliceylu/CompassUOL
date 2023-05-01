import os
from pathlib import Path
from glob import glob
import boto3
from datetime import datetime


s3 = boto3.client(
    's3',
    aws_access_key_id="ASIA2CPG5L5WWK5QK6MB",
    aws_secret_access_key="fOfKb3qiCljC5kDz6NEReTk+qzL5ak8NfmhPnHOw",
    aws_session_token="IQoJb3JpZ2luX2VjEKH//////////wEaCXVzLWVhc3QtMSJGMEQCIEH9CCjaUXbJ1/el6/LZcXK3z/il4WWpKvehpDJ9uQR6AiAH0dh+4IgbjE/hMvPVa/zen2KpQG1HD0EIVfK3DeJGzCqeAwiq//////////8BEAAaDDY5MjUxMDg3NTUwMSIMCRMBt1zy8vMW8frmKvIC3DqLyh1FXWMZsXHc/FOoGYF5PqfeEAVH4OAyVAZTvAAZW86EpqKaPdRhSIxgHTZ8Emy8MZIFjZraO8mdu+vNA/w3DopYc+MzRuDZFS19n25obRMtyDhlTqvbvNm4vCkFuxgF9AmjdnxZd7UYB/jPwM9wBaeyNR3/OVmlSVn8gZUb9mAnv5RQoDKTQ9pyCxs8KgFyKSpOafgwGadYMMtf+miCN1I8fqegNz+Z0SduT73IfubNCeAKWimx7d1o8dDG3/A07yzFthr5KGcfSfHGfvEad35C+TtpQ/AZUXw223qLMojdtsipVDkxzazbafMVutaT3RyGQG3zDMHtlqtNn1FxcIHoI0SXVgocIjTJpNsB4w8kD5axKYXy9ZxpEy8ScYZpLZmABBB0heUNrwnNf8+NfPpSnJ6CbahX/and6/0Z6IyaXJPT0ZAorsraRlObcWLOZC9nI5uf08EmsaZ0aB2xWHTw1CXTESUMxR0L12iIETCU1b+iBjqnAXm/EIqY9ZwfLXiOxbECLgSgvkoQC1kOYpJ0tQDeaHugdPeM88M02DLd17KQIvwnD0D/GCHt2laEINlTS7bnsnh2JJWdprLgIPB9DHpO1s3oIcMLa1xljoY1bjY/ekt/xsMUwcXXWwUC8BHfXe8aLsZXQ2BlmYQzhdkxmoLmtCz3SziAPxvysudmW06svcDd1+rOCp9DEZskpCkApO+whAYZJAV1Ohvd")

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

