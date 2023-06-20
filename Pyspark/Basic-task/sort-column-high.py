from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-21").getOrCreate()

#21.Sort the column ‘high’ in the DF and display the result.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.sort(['High'], ascending=[True]).show()
