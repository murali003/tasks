from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-6").getOrCreate()

#6.Apply Limit to the DataFrame and display the values.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
result = data.limit(10).toPandas()
print(result.to_string())