# ALTER TABLE Equivalent

# Add New Field

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully")

db = client["college"]

collections = db["students"]

student = [{
    "name":"Razin",
    "roll-no": 1,
    "Gender":"male",
    "email":"razinmulani01@gmail.com"
    },
    {
    "name":"Sami",
    "roll-no": 2,
    "Gender":"male",
    "email":"saminulani01@gmail.com"
    },
    {
    "name":"Shabnoor",
    "roll-no": 3,
    "Gender":"male",
    "email":"shabnoormulani01@gmail.com"
    }]
result = collections.insert_many(student)
for data in collections.find():
    print(data)

for data in student:
    collections.update_many(
        {},
        {"$set":{"email":" "}}
        )

# Rename data
collections.update_many(
    {},
    {"$rename":{"name":"student_name"}}
    )

for data in collections.find():
    print(data)
print("rename")

# remove data
collections.update_many(
    {},
    {"$unset":{"email":""}}
    )
for data in collections.find():
    print(data)
