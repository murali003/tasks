from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("tasks").getOrCreate()

df = spark.read.csv("/home/snegha/Downloads/example.csv", header=True)
df.createOrReplaceTempView("data1")
df1 = spark.sql("select * from data1").show()
#spark.sql("ALTER TABLE data drop StudentId").show()
#df1.write.csv("/home/snegha/Downloads/output4.csv", header=True)
df1.write.option("header",True).csv("/home/snegha/Downloads/output5.csv")







