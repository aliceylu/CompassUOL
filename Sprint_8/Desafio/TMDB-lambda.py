import requests
import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    S3_BUCKET_NAME = "aylu-compasso"
    s3 = boto3.client("s3")
    now = datetime.now()
    datenow = now.strftime("%Y/%m/%d")

    responses = list()
    apikeys = ['640146', '420808', '447365', '594767', '76600', '634649', '385128', '635302', '875104', '299536', '118340', '299536', '384018', '299534', '335988', '283995', '290271', '335988', '87101', '284053', '118340', '24428', '177572', '11', '99861', '22', '120', '121', '122', '564', '9732', '1893', '95', '658']
    
    for apikey in apikeys:
        url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(apikey)
    
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NjE4NDNiNzEwMDExZjdjZmI0YzY4NWFlZGVlYmVjMyIsInN1YiI6IjY0NTJjMTA5ZDhmNDRlMGRiMTlmMmNmZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.cGPY-9InHNK0nGLXozwEH6hEMZNX735DCN1RjdOq0rI"
        }
    
        response = requests.get(url, headers=headers)
    
        json_data = response.json()
        
        s3.put_object(Body=json.dumps(json_data), Bucket=S3_BUCKET_NAME, Key="Raw/TMDB/JSON/{}/{}.json".format(datenow, apikey))
