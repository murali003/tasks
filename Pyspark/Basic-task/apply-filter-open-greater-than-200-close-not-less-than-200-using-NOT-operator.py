from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("task-14").getOrCreate()

#19."Apply filter when ‘open’ is greater than 200 and  when ‘close’  is not less than 200 using NOT operator."
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)
data.filter((data.Open > 200) & (~(data.Close < 200))).show()
