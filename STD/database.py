# database.py
from pymongo import MongoClient
from config import MONGO_URI,DATABASE_NAME,collection_name

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[collection_name]

print("MongoDB Connected Successfully!")

# Insert Student Name
def insert_student(data):
    return collection.insert_one(data)

# Search Student
def search_student(search_by, search_text):
    query = {
            search_by:{
                "$regex": search_text,
                "$options":"i"
                }
        }
    return collection.find(query)

# Find One Student
def find_student(student_id):
    return collection.find_one({"student_id":student_id})

# Update Student
def update_student(student_id, new_data):
    return collection.update_one(
        {"student_id":student_id},
        {"$set": new_data}
        )

# Delete Student
def delete_student(student_id):
    result = collection.delete_one(
        {"student_id":student_id}
        )
    print(result.deleted_count)

# Get all Students
def get_all_students():
    return collection.find()

def get_student(student_id):
    return collection.find_one({"student_id": student_id})

# Count Students
def count_students():
    return collection.count_documents({})

# Close Connection
def close_connection():
    client.close()

def collection_drop():
    return collection.drop()

# Restore  Student Into MongoDB

def restore_students(student_list):

    collection.delete_many({})

    if student_list:
        collection.insert_many(student_list)
