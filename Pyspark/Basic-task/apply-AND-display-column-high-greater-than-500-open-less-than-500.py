from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("task-17").getOrCreate()

#17."Apply where and display the column name ‘high’ greater than 500 and ‘open’ less than 500 and display the result."
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
#data.filter((data.High > 500) & (data.Open < 500)).show()

data.filter('High > 500 AND Open < 500').show(truncate=True)