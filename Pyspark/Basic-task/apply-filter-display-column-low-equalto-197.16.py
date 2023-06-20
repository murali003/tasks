from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-18").getOrCreate()

#18.Apply filter and display the result when ‘Low’ column value is equal to 197.16 using comparison operator.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.filter(data.Low == 197.16).show()
