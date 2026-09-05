# All CRUD Method perform

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully!")

db = client["BioData"]

collection = db["employes"]

# Input data
employe = [{
    "name":"razin",
    "age":21,
    "e-id":1,
    "email":"razinmulani01@gmail.com"
    },{
    "name":"razin",
    "age":21,
    "e-id":2,
    "email":"samimulani01@gmail.com"
    }]
'''
result = collection.insert_many(employe)
for data in collection.find():
    print(data)
#print(result)
'''
'''
# Find The Data
for data in collection.find():
    print(data)

#find the ID's

print("ID's:",result.inserted_ids)
'''
# Update The Data
'''
collection.update_many(
    {"e-id":2},
    {"$set":{"name":"Sami"}}
    )

for data in collection.find():
    print(data)

'''
print("=======================================================")
# Delete The Data
'''
collection.delete_one(
    {"name":"razin"}
    )

for data in collection.find():
    print(data)

'''
# Add Section(email)
'''
for data in employe:
    collection.update_many(
        {},
        {"$set":{"email":" "}}
        )
'''
# rename
'''
for data in employe:
    collection.update_many(
        {},
        {"$rename":{"name":"employe_name"}}
        )

for data in collection.find():
    print(data)
'''
# remove
'''
collection.update_many(
    {},
    {"$unset":{"email":" "}}
    )
for data in collection.find():
    print(data)

'''

#Destroy the table
'''
db.employes.drop()
print("Drop The Table")

for data in collection.find():
    print(data)
'''
# Show all data base
'''
database = client.list_database_names()
print(database)
'''
# destroy the data base
client.drop_database("BioData")

for data in collection.find():
    print(data)


database = client.list_database_names()
print(database)



