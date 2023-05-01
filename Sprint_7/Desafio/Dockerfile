FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install boto3

CMD ["python3", "./upload_files.py"]