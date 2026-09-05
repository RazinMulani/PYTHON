# Update the value
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

# updated the value
result = collections.insert_many(student)
collections.update_many(
    {"roll-no":3},
    {"$set":{"Gender":"female"}}
    )
for data in collections.find():
    print(data)




    
