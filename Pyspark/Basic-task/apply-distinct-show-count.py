from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-10").getOrCreate()

#10.Apply distinct and show the count

data = spark.read.csv("D:\pyspark-programs\Basic-task\Sales-info.csv", header=True)
print(data.select("company").distinct().count())