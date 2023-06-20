from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-9").getOrCreate()

#9.Read the CSV and select the particular column and display distinct values
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data1 = spark.read.csv("D:\pyspark-programs\Basic-task\Sales-info.csv", header=True)
data.select("High").distinct().show()
data1.select("company").distinct().show()