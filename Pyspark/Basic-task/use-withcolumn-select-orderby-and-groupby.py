from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("task-25").getOrCreate()

#25.How to use the withcolumn then select the order by and group by.
data = spark.read.csv("D:\pyspark-programs\Basic-task\Sales-info.csv", header=True)

# result = (
#   data.withColumn("Sales",col("Sales").cast("Integer")).groupBy("Company").agg(sum("Sales"))
#   .orderBy("Company", ascending =[True])
# )
# result.show()
#df = data.withColumn("Sales",data["Sales"]).groupBy("Company").agg(sum("sales")).show()

df = data.withColumn("Sales",col("sales")).groupBy("Company").agg(sum("sales").alias("sales_of_company")).orderBy("sales_of_company",ascending=False).select("Company").show()


#df = data.select("Person").show()