from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("tasks").getOrCreate()
df = spark.read.csv("/home/snegha/Downloads/example.csv", header=True)

# # print(df.count())
df1 = df.orderBy("StudentAttendanceId").dropDuplicates(['StudentId'])
# # print(df1.count())
#
df2 = df1.na.replace('NULL','0')
df2.write.csv("/home/snegha/Downloads/output.csv", header=True)