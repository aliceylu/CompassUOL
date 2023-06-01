import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import row_number

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


dft = spark.read.parquet("s3://aylu-compasso/Trusted/tmdb.parquet/*.parquet")


df2 = dft.select('id', 'title', 'release_date')
df3 = dft.select('id', 'budget', 'revenue')
df4 = dft.select('id', 'popularity', 'vote_average', 'vote_count')


dfo = spark.read.parquet("s3://aylu-compasso/Trusted/omdb.parquet/*.parquet")

dfo.createOrReplaceTempView ("omdb")
dft.createOrReplaceTempView("tmdb")

dfkr1 = spark.sql("SELECT a.*, b.* FROM (select id, title, release_date, budget, revenue, popularity, vote_average, vote_count FROM tmdb) AS a RIGHT JOIN (select title, released, imdbrating, imdbvotes, metascore, boxoffice, tomatoes_rating FROM omdb) AS b ON a.title=b.title")

dfkr = dfkr1.select('id', 'popularity', 'vote_count', 'vote_average', 'imdbvotes', 'imdbRating', 'tomatoes_rating', 'metascore', 'boxoffice', 'budget', 'revenue')
    

DyF2 = DynamicFrame.fromDF(df2, glueContext, "DyF2")


glueContext.write_dynamic_frame \
    .from_options(
        frame = DyF2, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Refined/id.parquet"},
        format = "parquet")


DyF3 = DynamicFrame.fromDF(df3, glueContext, "DyF3")


glueContext.write_dynamic_frame \
    .from_options(
        frame = DyF3, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Refined/revenuebudget.parquet"},
        format = "parquet")
        
DyF4 = DynamicFrame.fromDF(df4, glueContext, "DyF4")


glueContext.write_dynamic_frame \
    .from_options(
        frame = DyF4, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Refined/ratings.parquet"},
        format = "parquet")
        
        
DyFkr = DynamicFrame.fromDF(dfkr, glueContext, "DyFkr")


glueContext.write_dynamic_frame \
    .from_options(
        frame = DyFkr, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Refined/keanureeves.parquet"},
        format = "parquet")


job.commit()