from pymongo import MongoClient
client = MongoClient('localhost')

#print(client)

db = client.Student
# print("db created")

col = db.Studentdetail


col.insert({ "name": "Krishva", "salary": 20000 })