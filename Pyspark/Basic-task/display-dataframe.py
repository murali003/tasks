from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-3").getOrCreate()

#3.Display the dataframe
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.show()