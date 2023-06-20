from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-8").getOrCreate()

#8.Apply count to df
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
print(data.count())