#Mini Project
#Python to mongodb
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

db = client["class"]
students = db["students"]

# Add Student Info
def add_student():
    roll =  int(input("Enter the Roll No."))
    name = input("Enter the name:")
    age = int(input("Enter The Age"))

    student = {
        "roll":roll,
        "name":name,
        "age":age
        }
    result = students.insert_one(student)
    print("Student Added Successfully!")

# View Students
def view_students():
    data = students.find()
    print("\nStudent Records")
    print("-" * 30)
    found =  False
    for student in data:
        found = True
        print("Roll No:", student["roll"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("-" * 30)
    if not found:
        print("No student Found")

# Search Student
def search_student():
    roll = int(input("Enter Roll No to Search:"))

    student = students.find_one({"roll":roll})
    if student:
        print("\nStudent Found")
        print("Roll No:", student["roll"])
        print("Student Name:", student["name"])
        print("Student Age:", student["age"])
    else:
        print("Student Not Found!")

# Update Student
def update_student():
    roll = int(input("Enter Roll no To Update:"))
    
    name = input("Enter The New Name")
    age = int(input("Enter The New Age"))

    result = students.update_one(
        {"roll":roll},
        {"$set":{"name":name,"age":age}}
        )
    if result.modified_count > 0:
        print("Student Update Successfully")
    else:
        print("Student Not Found!")
        

# Delete Student
def delete_student():
    roll = int(input("Enter Roll No To Delete:"))
    result = students.delete_one({"roll":roll})
    if result.deleted_count > 0:
        print("Student Delete Successfully!")
    else:
        print("Student Not Found!")

# Drop The Table
def drop_table():
    db.students.drop()
    print("drop table successfully")

# main menu
while True:
    print("\n=======STUDENT MANAGMENT SYSTEM=========")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Drop The Table")
    print("7. Exit")

    choice =  int(input("Enter Your Choice:"))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        drop_table()
    elif choice == 7:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")







    
