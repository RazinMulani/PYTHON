# Import Values in a Table
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Conectted Successfully")

db = client["Biodata"]
collections = db["employes"]
'''
# Input Value
employe = {
    "name":"Razin",
    "Emp-ID": 1,
    "Emp-Salary":"1lpa"
    }
# only one employe biodata
result = collections.insert_one(employe)
print("Inserted ID:",result.inserted_id)
print(result)

print("Add Value Successfully")
'''
# many employe biodata
employe = [{
    "name":"Razin",
    "Emp-ID": 1,
    "Emp-Salary":"1lpa"
    },
    {
    "name":"Sami",
    "Emp-ID": 2,
    "Emp-Salary":"2lpa"
    },
    {
    "name":"Shabnoor",
    "Emp-ID": 3,
    "Emp-Salary":"3lpa"
    }]
result = collections.insert_many(employe)
print(result)

for data in collections.find():
    print(data)


# Check all ID in at a time
print("Inserted ID's:",result.inserted_ids)
