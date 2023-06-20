from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-4").getOrCreate()

#4.Display the column name
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
print(data.columns)