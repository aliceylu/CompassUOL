import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as F
from pyspark.sql.functions import explode

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


df = spark.read\
    .option("multiline", "true")\
    .json("s3://aylu-compasso/Raw/TMDB/JSON/2023/05/28/*.json")
    
df = df.select('id', 'imdb_id', 'title', 'release_date', 'budget', 'revenue', 'popularity', 'vote_average', 'vote_count')
    

DynamicFrame = DynamicFrame.fromDF(df, glueContext, "DynamicFrame")


glueContext.write_dynamic_frame \
    .from_options(
        frame = DynamicFrame, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Trusted/tmdb.parquet"},
        format = "parquet")



job.commit()