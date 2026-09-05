# Delete Records

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Conectted Successfully...1")

db = client["college"]

collections = db["students"]

collections.delete_one(
    {"name":"Razin"}
    )

print("Delete Data Successfully ...!")

for data in collections.find(students):
    print(data)
