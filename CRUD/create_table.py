# Create Table

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
print("Conected Successfully...!")

db = client["Biodata"]
print("Create Biodata Successfully....!")

collections = db["employes"]
print("Collections Ready")
