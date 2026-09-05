# Practice

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully")

db = client["Biodata"]

collections = db["employes"]

employe = [{
    "name":"Razin",
    "age":22,
    "salary":"3lpa",
    "email":"razinmulani01@gmail.com"    
    },{
    "name":"Sami",
    "age":20,
    "salary":"4lpa",
    "email":"samimulani0161@gmail.com"
    },{
    "name":"Asjad",
    "age":21,
    "salary":"2lpa",
    "email":"asjadmulani0107@gmail.com"
    }]

result = collections.insert_many(employe)
for data in collections.find():
    print(data)
# Update the salary name:asjad

collections.update_one(
    {"name":"Asjad"},
     {"$set":{"salary":"5lpa"}}
    )

print("Update")

for data in collections.find():
    print(data)

# Delete employe name:sami

collections.delete_one(
    {"name":"Sami"}
    )
print("Delete")

for data in collections.find():
    print(data)

# Alter Table Equivalent:
# Add Field

for data in employe:
    collections.update_many(
        {},
        {"$set":{"email":" "}}
        )

# Rename
collections.update_many(
    {},
    {"$rename":{"name":"employe_name"}}
    )

for data in collections.find():
    print(data)
print("rename")

# Remove
collections.update_many(
    {},
    {"$unset":{"email":""}}
    )
for data in collections.find():
    print(data)

print("remove")

# Drop the table
db.employes.drop()
print("Table Drop")
for data in collections.find():
    print(data)


# Drop the Data Base
client.drop_database("Biodata")
print("Drop The Data Base")

for data in collections.find():
    print(data)

