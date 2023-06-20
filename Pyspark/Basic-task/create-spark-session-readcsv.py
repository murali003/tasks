from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task1").getOrCreate()

#1. Consider apple stock CSV file as input, Create a spark session and read the CSV file.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.show(truncate=True)
