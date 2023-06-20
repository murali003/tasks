from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("schema-tasks").getOrCreate()

result = spark.read.csv("D:\Pandas-programs\Read-csv\student-dataset.csv",header=True).show()