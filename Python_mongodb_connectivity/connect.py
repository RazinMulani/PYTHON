from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully")

# DataBase Created
db = client["college"]

print("Database Created")

# Table Created or Collection Created
collection = db["students"]

print("Table created")

# insert The value

student = [{"name" : "Shabnoor",
    "age" : 24,
    "city" : "Mahabaleshwar",
    "email":"shabnoor@gmail.com"
    },
    {
    "name" : "razin",
    "age" : 22,
    "city" : "Mahabaleshwar",
    "email":"razin@gmail.com"
    },{"name" : "sami",
    "age" : 20,
    "city" : "Mahabaleshwar",
    "email":"sami@gmail.com"}]


result = collection.insert_many(student)
print("inserted ID:",result.inserted_ids) # id of inserted row


for records in collection.find():
    print(records)
'''
# Find the row
data = collection.find_one({"name":"razin"})
print(data)
'''
'''
# Update the value
collection.update_one({"name":"razin"},{"$set":{"age":25}})
print("Updated")
 
data =  collection.find_one({"name":"razin"})
print(data)


collection.delete_one({"name":"razin"})
print("Deleted")



db.student.drop()
print("collection drop")
'''
'''
# Add Alter or Add email
collection.update_many(
    {},
    {"$set":{"email":""}}
)

print("column added")

'''
collection.update_many({},{"$rename":{"name":"student_name"}})
print("field renmae")

for records in collection.find():
    print(records)
