from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-15").getOrCreate()

#15."Apply where and display the column name ‘high’ greater than 500 and ‘open’ less than 500 and display the result."
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.where(data.High > 500).show()
data.where(data.Open < 500).show()