#With Login System
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["student_db"]

users = db["users"]
students = db["students"]

# Default Admin
if users.count_documents({"username": "admin"}) == 0:
    users.insert_one({
        "username": "admin",
        "password": "admin123"
    })

is_logged_in = False
#Login Function
def login():
    global is_logged_in

    username = input("Username: ")
    password = input("Password: ")

    user = users.find_one({
        "username": username,
        "password": password
    })

    if user:
        is_logged_in = True
        print("Login Successful")
    else:
        print("Invalid Username or Password")
#Logout Function
def logout():
    global is_logged_in
    is_logged_in = False
    print("Logged Out Successfully")
#Add Student
def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    age = int(input("Age: "))

    students.insert_one({
        "roll": roll,
        "name": name,
        "age": age
    })

    print("Student Added")
#View Students
def view_students():
    data = students.find()

    print("\nStudent Records")

    for s in data:
        print(
            s["roll"],
            s["name"],
            s["age"]
        )
#Search Student
def search_student():
    roll = input("Enter Roll No: ")

    student = students.find_one({
        "roll": roll
    })

    if student:
        print(student["roll"])
        print(student["name"])
        print(student["age"])
    else:
        print("Student Not Found")
#Update Student
def update_student():
    roll = input("Enter Roll No: ")

    name = input("New Name: ")
    age = int(input("New Age: "))

    result = students.update_one(
        {"roll": roll},
        {
            "$set": {
                "name": name,
                "age": age
            }
        }
    )

    if result.modified_count:
        print("Student Updated")
    else:
        print("Student Not Found")
#Delete Student
def delete_student():
    roll = input("Enter Roll No: ")

    result = students.delete_one({
        "roll": roll
    })

    if result.deleted_count:
        print("Student Deleted")
    else:
        print("Student Not Found")
#password change feature
def change_password():
    username = input("Enter Username: ")
    old_password = input("Enter Old Password: ")

    user = users.find_one({
        "username": username,
        "password": old_password
    })

    if user:
        new_password = input("Enter New Password: ")
        confirm_password = input("Confirm New Password: ")

        if new_password == confirm_password:
            users.update_one({"username": username},{"$set": {"password": new_password}})
            print("Password Changed Successfully!")
        else:
               print("Passwords Do Not Match!")
    else:
            print("Invalid Username or Old Password!")
#Main Menu
while True:

    if not is_logged_in:
        print("\n1. Login")
        print("2. Exit")

        choice = input("Choice: ")

        if choice == "1":
            login()

        elif choice == "2":
            break

    else:
        print("\n===== STUDENT MANAGEMENT =====")
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Change Password")
        print("7. Logout")

        choice = input("Choice: ")

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
           change_password()

        elif choice == "7":
           logout()
'''MongoDB Verify
show dbs

use student_db

show collections

db.users.find()

db.students.find().pretty()'''
