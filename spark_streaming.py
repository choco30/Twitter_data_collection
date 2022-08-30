from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField
from pyspark.sql.types import StringType,IntegerType
import json
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import col
from kafka import KafkaConsumer
import os
conn_string=os.environ.get("conn_string")

spark=SparkSession.builder.appName("Twitter_Structure_Streaming").config("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0").config("spark.mongodb.input.uri",conn_string).config("spark.mongodb.output.uri",conn_string).getOrCreate()
trend_schema=StructType([StructField("trend_name",StringType(),True),
                         StructField("twee_url",StringType(),True),
                         StructField("tweet_volume",IntegerType(),True)])
df=spark.readStream.format("kafka").option("kafka.bootstrap.servers","localhost:9092").option("subscribe","twitter_api").option("startingoffset","latest").load()
new_df=df.select(col('value').cast('string'),col("Timestamp").cast("String").alias("Fetch_Time"))
final_df=new_df.select(from_json(col('value'),trend_schema).alias("trends"),col("Fetch_Time")).select("trends.*")
final_df.printSchema()
df2=final_df.withColumn("tweet_volume",when(col("tweet_volume") == None,5000).otherwise(col("tweet_volume")))
'''df2.writeStream\
      .format("csv")\
      .option("header",True)  \
      .outputMode("append")\
      .option("path","C:\\Users\\ritvi\\Desktop\\spark\\data")\
      .option("checkpointLocation","C:\\Users\\ritvi\\Desktop\\spark\\checkpoint")\
      .start()\
      .awaitTermination()\
      '''
def write_row(batch_df,batch_id):
    batch_df.write.format("mongo").mode("append").save()
df2.writeStream.foreachBatch(write_row).start().awaitTermination()



