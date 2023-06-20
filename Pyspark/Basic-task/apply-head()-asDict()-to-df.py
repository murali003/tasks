from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-7").getOrCreate()

#7.Apply head() and asDict() to df
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
print(data.head(4))
print(data.head(5)[2].asDict())
