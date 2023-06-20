from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.context import SparkContext
import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder.appName("pyspark-tasks").getOrCreate()

#Dataframe SQL query
data = spark.read.csv("D:\pyspark-programs\Basic-task\Apple-stock.csv", header=True)

#1.Consider apple stock CSV file as input, Create a spark session and read the CSV file.
#data.show()

#2.Create a temporary view name as stock
#data.createOrReplaceTempView("stock")
#spark.sql("select * from stock").show()

#3.Run a simple SQL query that returns a DataFrame.
#spark.sql('''select 'spark' as hello ''').show()


#4.How many entries in the Close field are higher than 500.
#print(data.filter(data.Close>500).count())




#CSV
#5.Read the Sample_File csv
data2 = spark.read.csv("D:\pyspark-programs\Dataframe-SQL-query\Sample_File.csv", header=True)
#data2.show()

#6.Drop empty rows
#data2.dropna().show()

#7.Fill empty rows with NA
#data2.fillna("NA").show()

#8.Replace NA rows with Values
#data2.na.fill(value=0).show()
#data2.replace("NA","123").show()


#9.Drop duplicate values
#data2.drop_duplicates().show()


#10.Add new column with static data
#data2.withColumn("value",lit("hi")).show()

#11.Drop a column
#data2.drop("value").show()

#12.Select particular columns
#data2.select("Adj Close").show()

#13.Filtering the data on particular values
#data2.select("Low").filter(data2["Low"] >=92).show()




#JSON
#14.Read the Dataframe_Sql Json file and remove the duplicates.
data1 = spark.read.json("D:\pyspark-programs\Dataframe-SQL-query\Dataframe_sql.json")
#data1.drop_duplicates().show()


#15.Counts the number of distinct rows in dataframe
#print(data1.distinct().count())

#16.Replacing null values
#data1.na.fill(value=0).show()



#17.Return new dataframe replacing one value with another



#18.Show all entries in title, author, rank, price columns.
#data1.select('title','author','rank','price').show()

#19.Show title and assign 0 or 1 depending on title
#data1.select('title',when(data1.title != 'ODD HOURS',1).otherwise(0)).show(10)


#20.Show rows with specified authors such as "John Sandford", "Emily Giffin".
#data1.select(data1["author"].isin("John Sandford", "Emily Giffin")).show(10)


#21.Show author and title is TRUE if title has " THE " word in titles
#data1.select('author','title',data1.title.contains('THE')).show(10)

#22.Show author and title is TRUE if the title starts with " THE " word.
#data1.select('author','title',data1.title.startswith('THE')).show(10)

#23.Show author and title is TRUE if the title ends with " NT " word.
#data1.select('author','title',data1.title.endswith('THE')).show(10)

#24."Select author extracted the text between (1,3),(3,6) and (1,6) & gave column names as title 1, title 2 and title 3."
#data1.select(data1.author.substr(1,3)).alias("title1").show()
#data1.select(data1.author.substr(3,6)).alias("title2").show()
#data1.select(data1.author.substr(1,6)).alias("title3").show()

#25.Add a column name as ‘new_column’ and give the value ‘This is a new column’
#data1.withColumn('new_column',lit('This is a new column')).show()


#26.Update column name 'amazon_product_url' with 'URL'
#data1.withColumnRenamed('amazon_product_url','URL').show()

#27.Remove column ‘new_column’ from the DF.
#data1.drop('new_column').show()


#28.Group by author, count the books of the authors in the groups
#data1.groupBy("author").count().show()




#29.Filtering entries of title, Only keeps records having value 'THE HOST'.
#data1.filter(data1["title"] == 'THE HOST').show()


#30.Create sample DF and Convert DF into an RDD.
dataframe = [('Snegha',10000), ('Krishva',12000),('Ammu',15000)]
result = spark.createDataFrame(dataframe,["Name","Salary"])
#result.show()
#rdd = result.rdd
#print(rdd.collect())

#31.Converting dataframe into a RDD of string.



#32.Obtaining contents of df as pandas.
#print(result.toPandas())

#33.Understand the nested json object try to write the schema to flatten json



