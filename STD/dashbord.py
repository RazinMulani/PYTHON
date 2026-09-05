# dashbord.py

# Import Library's
import os
import json
from tkinter import *
from tkinter import ttk
from student import (
    add_student,
    edit_student,
    remove_student,
    search_student
    )
from database import (
    get_all_students,
    restore_students,
    get_student
    )
from PIL import Image, ImageTk
from tkinter import filedialog
from openpyxl import Workbook
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from tkinter import messagebox

# Functions

# Clear Field
def clear_fields():
    student_id.set("")
    name.set("")
    age.set("")
    gender.set("Male")
    course_box.current(0)
    phone.set("")
    email.set("")
    address.delete("1.0",END)
    photo_path.set("")
    photo_label.config(image="", text="No Image")
    photo_label.image = None

    
# Upload Photo Functio
def upload_photo():
    filename = filedialog.askopenfilename(
        title="Select Student Photo",

        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg")
            ]
        )
    if filename:
        photo_path.set(filename)
        show_photo(filename)
        
# Show Treeview
def show_students():

    # Delete Old Data From Treeview
    student_table.delete(*student_table.get_children())

    # Get all Students From MongoDB
    students = get_all_students()

    # Insert each Student Into Treview
    for student in students:

        student_table.insert(
            "",
            END,
            values=(
                student.get("student_id"),
                student.get("name"),
                student.get("age"),
                student.get("gender"),
                student.get("course"),
                student.get("phone"),
                student.get("email"),
                student.get("address"),
                student.get("photo")
                )
            )
# Save Student Data
def save_student():
    student = {
        "student_id": student_id.get(),
        "name":name_entry.get(),
        "age":age_entry.get(),
        "gender":gender.get(),
        "course":course_box.get(),
        "phone":phone_entry.get(),
        "email":email_entry.get(),
        "address":address.get("1.0",END).strip(),
        "photo":photo_path.get()
        }
    # Save Student In MongoDB
    add_student(student)

    # Reload Treeview
    show_students()

    # Clear all Inputs fields
    clear_fields()


# get_cursor function
def get_cursor(event):
    # Get Selected Row
    cursor = student_table.focus()

    content = student_table.item(cursor)

    row = content["values"]

    if row:

        student_id.set(row[0])
        name.set(row[1])
        age.set(row[2])
        gender.set(row[3])
        course.set(row[4])
        phone.set(row[5])
        email.set(row[6])
        #address.set(row[7])
        
        student = get_student(student_id.get())
        print(student)
        if student:
            address.delete("1.0", END)
            address.insert(END, student.get("address", ""))

            photo_path.set(student.get("photo", ""))

            show_photo(student.get("photo", ""))

    

    
    

# Update Function
def update_data():
    student={
        "student_id": student_id.get(),
        "name":name_entry.get(),
        "age":age_entry.get(),
        "gender":gender.get(),
        "course":course_box.get(),
        "phone":phone_entry.get(),
        "email":email_entry.get(),
        "address":address.get("1.0",END).strip(),
        "photo":photo_path.get()
        }
    edit_student(student)
    show_students()
    clear_fields()

# Delete Function
def delete_data():
    if student_id.get() == "":
        messagebox.showerror(
            "Error",
            "Please select a student!"
            )
        return

    answer = messagebox.askyesno(
        "Confirm",
        "Do you want to delete this student?"
        )

    if answer:
        remove_student(student_id.get())

        show_students()

        clear_fields()

# Search Student
def search_data():

    #Clear Old Data
    student_table.delete(*student_table.get_children())

    #get search values
    field_map={
        "Student Id": "student_id",
        "Name": "name",
        "Phone": "phone",
        "Course": "course"
        }
    field = field_map[search_by.get()]
    text = search_entry.get().strip()

    # validation
    if text =="":
        messagebox.showerror(
            "Error",
            "Please Enter Something to Search!"
            )
        return

    # Seaarch MongoDB
    students = search_student(field, text)

    # Display Results
    for student in students:
        student_table.insert(
            "",
            END,
            values=(
                student["student_id"],
                student["name"],
                student["age"],
                student["gender"],
                student["course"],
                student["phone"],
                student["email"],
                student.get("address", "")
                )
            )
        
# Export Data in Excel
def export_excel():
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Students"

    # Heading
    sheet.append([
        "Student ID",
        "Name",
        "Age",
        "Gender",
        "Course",
        "Phone",
        "Email",
        "Address"
        ])
    # Read MongoDB Data
    students = get_all_students()

    for student in students:

        sheet.append([
            student.get("student_id"),
            student.get("name"),
            student.get("age"),
            student.get("gender"),
            student.get("course"),
            student.get("phone"),
            student.get("email"),
            student.get("address")
            ])

    workbook.save("students.xlsx")

    messagebox.showinfo(
        "Success",
        "Student data exported successfully!"
        )

# Export Pdf
def export_pdf():
    pdf = SimpleDocTemplate("students.pdf")

    data = []

    #heading
    data.append([
        "ID",
        "Name",
        "Age",
        "Gender",
        "Course",
        "Phone",
        "Email"
        ])

    #read mongo data
    students = get_all_students()

    for student in students:
        data.append([
            student.get("student_id"),
            student.get("name"),
            student.get("age"),
            student.get("gender"),
            student.get("course"),
            student.get("phone"),
            student.get("email")
            ])
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0),colors.grey),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("BOTTOMPADDING", (0,0),(-1,0),10)
        ]))
    pdf.build([table])

    messagebox.showinfo(
        "Success",
        "PDF Exported Successfully!"
        )


# backup_json() Function
def backup_json():
    students = get_all_students()

    backup_data = []

    for student in students:
        # remove MongoDB ObjectID
        student.pop("_id", None)

        backup_data.append(student)

    with open("backup.json", "w") as file:
        json.dump(
            backup_data,
            file,
            indent=4
            )

    messagebox.showinfo(
        "Success",
        "Backup Created Successfully!"
        )

# restore_json()
def restore_json():
    try:
        with open("backup.json","r") as file:
            students = json.load(file)

        restore_students(students)

        show_students()

        messagebox.showinfo(
            "Success",
            "Database Restored Successfully!"
            )
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "backup.json file not found!"
            )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
            )

# show_photo() Function
def show_photo(path):
    try:
        print("show_photo called")
        if not path or not os.path.exists(path):
            photo_label.config(image="", text="No Image")
            return

        image = Image.open(path)
        image = image.resize((140, 140), Image.Resampling.LANCZOS)

        photo = ImageTk.PhotoImage(image)

        photo_label.config(image=photo, text="")
        photo_label.image = photo

        print("Image loaded successfully")

    except Exception as e:
        print("ERROR:", e)
    
# main window

root = Tk()

root.title("Student Managment System")
root.geometry("1350x700")
root.resizable(True,True)
root.configure(bg="white")

# Heading

title = Label(
    root,
    text="Student Managment System",
    fg= "white",
    bg="#0B5394",
    font=("Arial",20,"bold"),
    pady=10
    )
title.pack(fill=X)## Fill Complete Width

#left frame
student_frame = LabelFrame(
    root,
    text="Student Details",
    font=("Arial",12,"bold"),
    bg="white",
    padx = 10,
    pady =10
    )
student_frame.place(
    x = 20,
    y = 70,
    width = 500,
    height = 650
    )



# Student Details
# Student ID
Label(
    student_frame,
    text="Student ID",
    font=("Arial",11),
    bg="white"
    ).grid(row=0,column=0,padx=10,pady=10,sticky=W)

student_id = StringVar()
student_id_entry = Entry(
    student_frame,
    textvariable =student_id,
    font=("Arial",11),
    width=25
    )

student_id_entry.grid(row=0, column=1, padx=10, pady=10)

#Student Name
Label(
    student_frame,
    text="Student Name",
    font=("Arial",11),
    bg="white"
    ).grid(row=1,column=0,padx=10,pady=10,sticky=W)

name = StringVar()
name_entry = Entry(
    student_frame,
    textvariable =name,
    font=("Arial",11),
    width=25
    )

name_entry.grid(row=1, column=1, padx=10, pady=10)
# Student Age

Label(
    student_frame,
    text="Student Age",
    font=("Arial",11),
    bg="white"
    ).grid(row=2,column=0,padx=10,pady=10,sticky=W)

age = StringVar()
age_entry = Entry(
    student_frame,
    textvariable =age,
    font=("Arial",11),
    width=25
    )

age_entry.grid(row=2, column=1, padx=10, pady=10)
# Students Gender 
Label(
    student_frame,
    text="Student Gender",
    font=("Arial",11),
    bg="white"
    ).grid(row=3,column=0,padx=10,pady=10,sticky=W)

gender = StringVar()
Radiobutton(
    student_frame,
    text="Male",
    variable=gender,
    font=("Arial",11),
    value="Male",
    bg="white"
    ).grid(row=3, column=1,sticky=W)

Radiobutton(
    student_frame,
    text="Female",
    variable=gender,
    font=("Arial",11),
    value="Female",
    bg="white"
    ).grid(row=3,column=1,padx=80,sticky=W)

# Course (Combobox)
Label(
    student_frame,
    text="Course",
    font=("Arial",11),
    bg="white"
    ).grid(row=4,column=0,padx=10, pady=10,sticky=W)

course =StringVar()

course_box = ttk.Combobox(
    student_frame,
    textvariable=course,
    width=23,
    state="readonly"
    )
course_box["values"]=(
    "Computer Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Electronics Engineering",
    "Information Technology"
    )
course_box.grid(row=4,column=1,padx=10,pady=10)
course_box.current(0)

# Phone
Label(
    student_frame,
    text="Student Phone Number",
    font=("Arial",11),
    bg="white"
    ).grid(row=5,column=0,padx=10,pady=10,sticky=W)

phone = StringVar()
phone_entry = Entry(
    student_frame,
    textvariable =phone,
    font=("Arial",11),
    width=25
    )

phone_entry.grid(row=5, column=1, padx=10, pady=10)

# Email
Label(
    student_frame,
    text="Student Email",
    font=("Arial",11),
    bg="white"
    ).grid(row=6,column=0,padx=10,pady=10,sticky=W)

email = StringVar()
email_entry = Entry(
    student_frame,
    textvariable =email,
    font=("Arial",11),
    width=25
    )

email_entry.grid(row=6, column=1, padx=10, pady=10)

# Address
Label(
    student_frame,
    text="Student Address",
    font=("Arial",11),
    bg="white"
    ).grid(row=7,column=0,padx=10,pady=10,sticky=NW)

address = Text(
    student_frame,
    width=25,
    height=4,
    font=("Arial",11)
    )
address.grid(row=7, column=1, padx=10, pady=10)

#upload Photo
Label(
    student_frame,
    text="Photo",
    font=("Arial",11),
    bg="white"
    ).grid(row=8,column=0, padx=10, pady=10, sticky=W)

photo_path = StringVar()

photo_entry =Entry(
    student_frame,
    textvariable = photo_path,
    width=15,
    state="readonly",
    font=("Arial",11)
    )
photo_entry.grid(row=8, column=1, padx=10, pady=10)

photo_label = Label(
    student_frame,
    text="No Image",
    bg="yellow",
    relief="solid",
    bd=2,
)

photo_label.grid(
    row=0,
    column=2,
    rowspan=8,
    padx=20,
    pady=10
)
# Upload Button

upload_btn = Button(
    student_frame,
    text="Browse",
    bg="red",
    width =8,
    command=upload_photo
    )

upload_btn.grid(row=9, column=1, padx=5,pady=10)

# Right Farame
record_frame = LabelFrame(
    root,
    text="Student Records",
    font=("Arial",12,"bold"),
    bg="white",
    padx=10,
    pady=10
    )
record_frame.place(
    x=460,
    y=70,
    width=870,
    height=600
    )
# Search Frame

search_frame = Frame(
    record_frame,
    bg="white"
    )
search_frame.pack(fill=X, pady=5)
# Search Label
Label(
    search_frame,
    text="Search By",
    font=("Arial",11,"bold"),
    bg="white"
    ).grid(row=0, column=0, padx=5, pady=5)
# Search Combobox
search_by = StringVar()

search_combo = ttk.Combobox(
    search_frame,
    textvariable = search_by,
    width=18,
    state="readonly"
    )

search_combo["values"]=(
    "Student Id",
    "Name",
    "Phone",
    "Course"
    )

search_combo.current(0)
search_combo.grid(row=0,column=1, padx=5)

#Search Entry
search_text =StringVar()

search_entry = Entry(
    search_frame,
    textvariable=search_text,
    width=25,
    font=("Arial",11)
    )

search_entry.grid(row=0, column=2, padx=5)

# Search button
search_btn =  Button(
    search_frame,
    text="Search",
    width=10
    )
search_btn.grid(row=0,column=3,padx=5)

# Search Show All Button
show_all_btn = Button(
    search_frame,
    text="Show All",
    width=10
)

show_all_btn.grid(row=0, column=4, padx=5)

# 

# Treeview
# Vertical Scroll Bar
scroll_y = Scrollbar(record_frame, orient=VERTICAL)
#Horizontal Scroll Bar
scroll_x = Scrollbar(record_frame, orient=HORIZONTAL)

# Create Treeview
student_table = ttk.Treeview(
    record_frame,

    columns=(
        "student_id",
        "name",
        "age",
        "gender",
        "course",
        "phone",
        "email",
        "address",
        "photo"
        ),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
    )

# Connect Scroll Bar
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

# Create Heading
student_table.heading("student_id", text="Student ID")

student_table.heading("name", text="Name")

student_table.heading("age", text="Age")

student_table.heading("gender", text="Gender")

student_table.heading("course", text="Course")

student_table.heading("phone", text="Phone")

student_table.heading("email", text="Email")

student_table.heading("address", text="Address")

student_table.heading("photo", text="Photo")

# Set Colum Width

student_table.column("student_id", width=120)

student_table.column("name", width=150)

student_table.column("age", width=70)

student_table.column("gender", width=100)

student_table.column("course", width=180)

student_table.column("phone", width=120)

student_table.column("email", width=220)

student_table.column("address", width=200)

student_table.column("photo", width=200)

# Show Only Heading
student_table["show"]="headings"

# Desplay Treeview
student_table.pack(fill=BOTH, expand=True)

# Bind Treeview Click Event
student_table.bind(
    "<ButtonRelease-1>",
    get_cursor
    )


# Button Frame
button_frame = LabelFrame(
    root,
    text="Operations",
    font=("Arial", 12, "bold"),
    bg="white"
    )

button_frame.place(
    x=440,
    y=610,
    width=900,
    height=100
    )




# Create Operations Button
# Add Button
add_btn = Button(
    button_frame,
    text="Add",
    width=12,
    font=("Arial",10,"bold"),
    bg="#4CAF50",
    fg="white",
    command=save_student
    )

add_btn.grid(row=0,column=0,padx=5,pady=10)

# update Button
update_btn = Button(
    button_frame,
    text="Update",
    width=12,
    font=("Arial",10,"bold"),
    bg="#2196F3",
    fg="white",
    command=update_data
    )

update_btn.grid(row=0,column=1,padx=5,pady=10)

# Delete Button
delete_btn = Button(
    button_frame,
    text="Delete",
    width=12,
    font=("Arial",10,"bold"),
    bg="#F44336",
    fg="white",
    command=delete_data)

delete_btn.grid(row=0,column=2,padx=5,pady=10)
    
# Clear Button
clear_btn = Button(
    button_frame,
    text="Clear",
    width=12,
    font=("Arial",10,"bold"),
    bg="#FF9800",
    fg="white",
    command=clear_fields)

clear_btn.grid(row=0,column=3,padx=5,pady=10)

# Search Button
search_btn = Button(
    button_frame,
    text="Search",
    width=12,
    font=("Arial",10,"bold"),
    bg="#9C27B0",
    fg="white",
    command=search_data)

search_btn.grid(row=0,column=4,padx=5,pady=10)
# Show All Button
show_btn = Button(
    button_frame,
    text="Show All",
    width=12,
    font=("Arial",10,"bold"),
    bg="#009688",
    fg="white",
    command=show_students)

show_btn.grid(row=0,column=5,padx=5,pady=10)
# Exit Button
exit_btn = Button(
    button_frame,
    text="Exit",
    width=12,
    font=("Arial",10,"bold"),
    bg="black",
    fg="white",
    command=root.destroy
    )

exit_btn.grid(row=0,column=6,padx=5,pady=10)
# Export Excel
excel_btn = Button(
    button_frame,
    text="Export Excel",
    bg="green",
    fg="white",
    width=15,
    command=export_excel
    )
excel_btn.grid(row=0, column=7, padx=5)

# Export PDF
pdf_btn= Button(
    button_frame,
    text="Export PDF",
    bg="darkblue",
    fg="white",
    width=15,
    command=export_pdf
    )

pdf_btn.grid(row=1, column=0, padx=5)

# Backup btn
backup_btn = Button(
    button_frame,
    text="Backup",
    bg="purple",
    fg="white",
    width=15,
    command=backup_json
    )

backup_btn.grid(row=1,column=1,padx=5)

# Restore Button
restore_btn = Button(
    button_frame,
    text="Restore",
    bg="orange",
    fg="white",
    width=15,
    command=restore_json
    )

restore_btn.grid(row=1, column=2, padx=5, pady=5)
# cole function
show_students()
root.mainloop()




