from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-12").getOrCreate()

#12.Insert a new column called ‘Range’ after the low column.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Sales-info.csv", header=True)
data.withColumnRenamed("Company","Company Name").show()