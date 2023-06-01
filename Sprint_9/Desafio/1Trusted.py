import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as F
from pyspark.sql.functions import explode, regexp_replace


sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# TMDB
df = spark.read\
    .option("multiline", "true")\
    .json("s3://aylu-compasso/Raw/TMDB/JSON/2023/05/28/*.json")
    

df.createOrReplaceTempView ("tmdb")

df3 = spark.sql("select row_number() over(order by release_date) as id, title, release_date, budget, revenue, popularity, vote_average, vote_count from tmdb group by title, release_date, budget, revenue, popularity, vote_average, vote_count ")


DynamicFrame1 = DynamicFrame.fromDF(df3, glueContext, "DynamicFrame1")

glueContext.write_dynamic_frame \
    .from_options(
        frame = DynamicFrame1, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Trusted/tmdb.parquet"},
        format = "parquet")


# OMDB
dfo = spark.read\
    .option("multiline", "true")\
    .json("s3://aylu-compasso/Raw/OMD/JSON/2023/05/21/*.json")
    
dfo1 = dfo.withColumn("Ratings", explode("Ratings"))
dfo2 = dfo1.select('Title', 'Released', 'imdbRating', 'imdbVotes', 'Metascore', 'Ratings', 'BoxOffice', 'Awards')

dfo2.createOrReplaceTempView ("omdb")

df5 = spark.sql("SELECT title, released, imdbRating, imdbvotes, metascore, boxoffice, awards, kv1['Internet Movie Database'] AS imdb_rating, kv1['Rotten Tomatoes'] AS tomatoes_rating, kv1['Metacritic'] AS meta_rating FROM (SELECT title, released, imdbRating, imdbvotes, metascore, boxoffice, awards, map_concat(map(ratings.source, ratings.value)) AS kv1 FROM omdb GROUP BY title, released, imdbRating, imdbvotes, metascore, boxoffice, awards, ratings ORDER BY title, released, imdbRating, imdbvotes, metascore, boxoffice, awards, ratings)")
 
df6 = df5.withColumn('tomatoes_rating', regexp_replace('tomatoes_rating', '%', ''))

df6 = df6.withColumn('imdbRating', regexp_replace('imdbRating', '.', ''))

df7 = df6.select('title', 'released', 'imdbrating', 'imdbvotes', 'metascore', 'boxoffice', 'tomatoes_rating')


DynamicFrame2 = DynamicFrame.fromDF(df7, glueContext, "DynamicFrame2")

glueContext.write_dynamic_frame \
    .from_options(
        frame = DynamicFrame2, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Trusted/omdb.parquet"},
        format = "parquet")



# CSV
DynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://aylu-compasso/Raw/Local/CSV/movies/2023/05/01/movies.csv"]},
    format="csv",
    format_options={
        "withHeader": True,
        "inferSchema": True,
        "delimiter": '|'
    })

cdf = CdynamicFrame.toDF()
    
cdf2 = cdf.filter((F.col("tituloPincipal").rlike("Matrix") & F.col("nomeArtista").rlike("Keanu Reeves")) | (F.col("tituloPincipal").rlike("John Wick") & F.col("nomeArtista").rlike("Keanu Reeves")))


CDynamicFrame = DynamicFrame.fromDF(cdf2, glueContext, "CDynamicFrame")


glueContext.write_dynamic_frame \
    .from_options(
        frame = CDynamicFrame, 
        connection_type = "s3", 
        connection_options =  {"path":"s3://aylu-compasso/Trusted/moviescsv"},
        format = "parquet")




job.commit()