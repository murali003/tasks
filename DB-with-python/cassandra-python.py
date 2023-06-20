from cassandra.cluster import Cluster
cluster = Cluster()
#print(cluster)

#create keyspace
# session = cluster.connect()
# session.execute("create keyspace mykeyspace with replication={'class' : 'SimpleStrategy', 'replication_factor' : 3};")

#create table
# session = cluster.connect('mykeyspace')
# session.execute("create table Student(Id int,Name text, Age int, Gender text, Department text,primary key(Id)) ")

#insert
# session = cluster.connect("mykeyspace")
# session.execute("insert into Student(Id,Name,Age,Gender,Department) values (1,'Snegha',21,'F','IT');")
# session.execute("insert into Student(Id,Name,Age,Gender,Department) values (2,'Krishva',21,'M','IT');")
# session.execute("insert into Student(Id,Name,Age,Gender,Department) values (3,'Krishva',21,'M','CSE');")

#update
#session = cluster.connect('mykeyspace')
# session.execute("update Student set age=22 where id=1 ")

#select
# session = cluster.connect('mykeyspace')
# session.execute("select * from Student")

#delete
# session=cluster.connect('mykeyspace')
# session.execute("delete from Student where id=2")

#truncate
# session=cluster.connect('mykeyspace')
# session.execute("truncate table Student")

#drop
# session=cluster.connect('mykeyspace')
# session.execute("drop table Student")