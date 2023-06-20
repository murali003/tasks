from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-20").getOrCreate()

#20."Apply filter and display the result when ‘Low’ column value is equal to 197.16 using collect method."
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
print(data.filter(data.Low == 197.16).collect())
