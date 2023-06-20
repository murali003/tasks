from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-22").getOrCreate()

#22.Sort the column ‘high’ in the DF and display the result in the descending order.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.sort(['High'], ascending=[False]).show(truncate=False)



