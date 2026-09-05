# Drop Table and Data Base


# Drop Table
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully")

db = client["college"]

collections = db["students"]

student = [{
    "name":"Razin",
    "roll-no": 1,
    "Gender":"male"
    },
    {
    "name":"Sami",
    "roll-no": 2,
    "Gender":"male"
    },
    {
    "name":"Shabnoor",
    "roll-no": 3,
    "Gender":"male"
    }]

for data in collections.find():
    print(data)
    
db.students.drop()

print("Drop The Table")

for data in collections.find():
    print(data)



databases = client.list_database_names()
for db in databases:
    print(db)

client.drop_database("college")

print("Drop Database")
