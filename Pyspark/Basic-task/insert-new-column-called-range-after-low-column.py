from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task-11").getOrCreate()

#11.Insert a new column called ‘Range’ after the low column.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.withColumn("Range",data['high']-data['low']).select('high','low','range','close','volume','adj close').show()