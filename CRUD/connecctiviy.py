# Connectivity Python and Mongodb

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Conected Successfully")
