import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="Snegha",
  password="Snegha@123",
  database = "mydata"
 )
mycursor = conn.cursor()

#db creation
# mycursor.execute("create database mydata")
# print("db Created")

#table creation
# mycursor.execute("CREATE TABLE Student ( name VARCHAR(100), age INT,dept VARCHAR(100), address Varchar(100))")
# print("table created")

#check if table exists
#mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

#inserting data
# sql = "INSERT INTO Student (name,age,dept,address) VALUES (%s,%s,%s,%s)"
# val = [("snegha",21,"IT","abc"),
#        ("krishva",23,"CSE","dsa"),
#        ("kousi",32,"ECE","ert")]
#mycursor.execute(sql, val)
#print(mycursor.rowcount,"record added")

#inserting many rows
#mycursor.executemany(sql, val)
#print(mycursor.lastrowid,"records added")

#conn.commit()

#selecting and fetching all rows
# mycursor.execute("select * from Student")
# result = mycursor.fetchall()
# print(result)

#selecting and fetching one row
# mycursor.execute("select * from Student")
# result = mycursor.fetchone()
# print(result)

#selecting particular column
#mycursor.execute("SELECT name,address FROM Student")

#deleting record
# sql = "DELETE FROM Student WHERE address = 'abc'"
# mycursor.execute(sql)
# conn.commit()

#deleting using sql injecion
# sql = "DELETE FROM Student WHERE address = %s"
# addr = ("dsa", )
# mycursor.execute(sql, addr)
# conn.commit()

#updating
# sql = "UPDATE Student SET address = 'abc' WHERE address = 'ert' "
# mycursor.execute(sql)
# conn.commit()

#truncate
# sql = "TRUNCATE TABLE Student"
# mycursor.execute(sql)

#drop table
# sql = "DROP TABLE Student"
# mycursor.execute(sql)


# sql = "CREATE TABLE Data( name VARCHAR(100))"
# mycursor.execute(sql)

conn.close()