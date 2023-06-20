from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-5").getOrCreate()

#5.How to select Particular column from the CSV file and Display the respective values.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.select("Date").show()