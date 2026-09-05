#1. MongoDB Connection
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]
collection = db["students"]
#________________________________________
#2. Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    student = {
        "roll": roll,
        "name": name,
        "age": age
    }

    collection.insert_one(student)
    print("Student Added Successfully!")
#________________________________________
#3. View Students
def view_students():
    students = collection.find()

    print("\nStudent Records")
    print("-" * 30)

    for student in students:
        print("Roll No:", student["roll"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("-" * 30)
#________________________________________
#4. Search Student
def search_student():
    roll = input("Enter Roll No: ")

    student = collection.find_one({"roll": roll})

    if student:
        print("Student Found")
        print("Roll No:", student["roll"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
    else:
        print("Student Not Found")
#________________________________________
#5. Update Student
def update_student():
    roll = input("Enter Roll No to Update: ")

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))

    result = collection.update_one(
        {"roll": roll},
        {"$set": {"name": name, "age": age}}
    )

    if result.modified_count > 0:
        print("Student Updated Successfully!")
    else:
        print("Student Not Found")
#________________________________________
#6. Delete Student
def delete_student():
    roll = input("Enter Roll No to Delete: ")

    result = collection.delete_one({"roll": roll})

    if result.deleted_count > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found")
#________________________________________
#7. Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
