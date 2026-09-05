# Create Database

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully")

db = client["Biodata"]
print("Data Base Create Successfully")
