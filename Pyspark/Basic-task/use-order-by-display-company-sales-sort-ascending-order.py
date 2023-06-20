from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-22").getOrCreate()

#23.Use order by and display columns company and sales, sort in ascending order.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Sales-info.csv", header=True)
data.orderBy(["Company","Sales"],ascending = [True,True]).show()