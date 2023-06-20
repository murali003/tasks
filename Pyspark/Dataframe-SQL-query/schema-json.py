from pyspark.sql import SparkSession
from pyspark.sql.types import *
from  pyspark.sql import functions as f
spark = SparkSession.builder.appName("schema-tasks").getOrCreate()
schema1 = StructType().add("context",StructType()
                          .add("sid",StringType())
                          .add("did",StringType())
                          .add("cdata",ArrayType(StructType()
                                                 .add("type",StringType())
                                                 .add("id",StringType())))
                          .add("env",StringType())
                          .add("Channel",StringType())
                          .add("rollup",StructType()
                               .add("l1",StringType()))
                          .add("pdata",StructType()
                               .add("ver",StringType())
                               .add("pid",StringType())
                               .add("id",StringType()))
                          ).add("edata",StructType()
                                .add("pass",StringType())
                                .add("duration",FloatType())
                                .add("index",FloatType()))


result = spark.read.json("D:\pyspark-programs\Dataframe-SQL-query\schema_sample_file.json",multiLine=True,schema=schema1)
#result.printSchema()


df = result.withColumn("exploded",f.explode(result["context.cdata"]))
df = df.select("context.sid","context.pdata.id","exploded.type")
#df.show(truncate=False)

df.write.mode("overwrite").option("header",True).format("csv").save("D:\pyspark-programs\Dataframe-SQL-query\Result_Schema")

#df = result.select("edata.pass").show(truncate=False)
