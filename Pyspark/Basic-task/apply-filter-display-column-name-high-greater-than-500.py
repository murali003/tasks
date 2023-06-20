from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-13").getOrCreate()

#13.Apply filter and display the column name ‘high’ greater than 500.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.filter(data.High > 500).show()