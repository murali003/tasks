import psycopg2

conn = psycopg2.connect(
    user = 'postgres',
    password = 'Snegha@123',
    host = 'localhost',
    database = "mydata"
)
mycursor = conn.cursor()

#Db creation
#conn.autocommit = True
#db = ''' CREATE DATABASE mydata''';
#mycursor.execute(db)
#print("db Created")

#Table creation
# table = '''CREATE TABLE Student(
#                 Name CHAR(20),
#                 Age INT,
#                 Gender CHAR(20),
#                 Department CHAR(20)
#                 )'''
# mycursor.execute(table)
# print("table created")




#insert
# conn.autocommit = True
# mycursor.execute('''INSERT INTO Student (Name, Age, Gender, Department) VALUES ('Snegha',21, 'F', 'IT')''')
# mycursor.execute('''INSERT INTO Student(Name, Age, Gender, Department)VALUES('Kousi', 23, 'F', 'cse')''')
# mycursor.execute('''INSERT INTO Student(Name, Age, Gender, Department)VALUES('Krishva', 20, 'F', 'IT')''')
# mycursor.execute('''INSERT INTO Student(Name, Age, Gender, Department)VALUES('Sumathi', 19, 'F', 'IT')''')
# mycursor.execute('''INSERT INTO Student(Name, Age, Gender, Department)VALUES('Sobana', 24, 'F', 'ECE')''')
# conn.commit()
# print("records added")

#selecting
#mycursor.execute('''select * from Student''')
#fetching one row
#result = mycursor.fetchone()
#fetching all rows
#result = mycursor.fetchall()
#print(result)
#conn.commit()

#updating
# conn.autocommit = True
# update = "UPDATE Student SET Gender='M' WHERE Name='Krishva'"
# mycursor.execute(update)
# conn.commit()

#deleting
# delete = '''delete from Student where Age >=23 '''
# mycursor.execute(delete)
# conn.commit()

#truncating
# truncate = "truncate table Student"
# mycursor.execute(truncate)
# conn.commit()

#drop
# drop = "drop table Student"
# mycursor.execute(drop)
# conn.commit()


conn.close()