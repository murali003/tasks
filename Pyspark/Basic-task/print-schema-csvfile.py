from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task2").getOrCreate()

#2.Print the Schema of the CSV file.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv",header=True)
data.printSchema()