# Student.py
# import required library

from tkinter import messagebox

# import database function
from database import (
    insert_student,
    update_student,
    delete_student,
    search_student
    )

# Import logger
from logger import write_log

# Import Validation Function
from validation import(
    is_empty,
    valid_name,
    valid_age,
    valid_phone,
    valid_email
    )

def add_student(student_data):
    try:
        if is_empty(student_data["student_id"]):
            messagebox.showerror("Error","Student ID is Required.")
            return
        
        if is_empty(student_data["name"]):
            messagebox.showerror("Error", "Name is required.")
            return

        if not valid_name(student_data["name"]):
            messagebox.showerror("Error", "Enter a valid name.")
            return

        if not valid_age(student_data["age"]):
            messagebox.showerror("Error", "Enter a valid age.")
            return

        if not valid_phone(student_data["phone"]):
            messagebox.showerror("Error", "Enter a valid 10-digit phone number.")
            return

        if not valid_email(student_data["email"]):
            messagebox.showerror("Error", "Enter a valid email address.")
            return
        # insert into MongoDB
        insert_student(student_data)

        #write Log
        write_log("Student Added Successfully")

        # Success Message
        messagebox.showinfo(
            "Success",
            "Student Added Successfully."
            )
    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
            )

# Edit Student
def edit_student(student_data):
    try:
        update_student(
            student_data["student_id"],
            student_data
            )
        write_log("Student Update Successfully")

        messagebox.showinfo(
            "Success",
            "Student Update Successfully!"
            )

    except Exception as error:
        messagebox.showerror(
            "Database Error",
            str(error)
            )

# Remove Student
def remove_student(student_id):
    try:
        delete_student(student_id)

        write_log("Student Deleted Successfully")

        messagebox.showinfo(
            "Success",
            "Student Deleted Successfully!")
    except Exception as error:
        messagebox.showerror(
            "Database Error",
            str(error)
            )



