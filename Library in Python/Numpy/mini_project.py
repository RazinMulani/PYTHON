# Mini Project In Numpy

import numpy as np

marks = np.array([
    [78, 85, 69, 90],
    [65, 72, 80, 75],
    [92, 88, 95, 90],
    [45, 55, 48, 60],
    [81, 79, 85, 88]
    ])
def std_marks():
    print("Student Marks: \n",marks)
std_marks()
# Basic Information
# Display: Number of Students:, Number of Subjects:, Array Dimensions:, Total Elements:, Data Type:
def basic_info():
    print("\nNumber of Students: ",marks.shape[0])
    print("Number of Subjects: ",marks.shape[1])
    print("Array Dimension: ",marks.ndim)
    print("Total Elements: ",marks.size)
    print("Shape of Array: ",marks.shape)
    print("Data Type Array: ",marks.dtype)
basic_info()

# Q2. Total Marks of Each Student
# Calculate the total marks for every student.

def std_total_marks():
    print("\nTotal Marks Of Each Students: ")
    total_marks = np.sum(marks, axis = 1)
    num = 1
    for data in total_marks:
        print(f"Student {num}:",data)
        num += 1
std_total_marks()


# Q3. Average Marks
# Calculate the average marks of every student.

def std_average():
    print("\nAverage Marks Of Each Students: ")
    avg_marks = np.mean(marks, axis = 1)
    num = 1
    for data in avg_marks:
        print(f"Student {num}: ",data)
        num += 1
std_average()

# Q4. Highest and Lowest Marks
# Find: Highest mark in the entire array, Lowest mark in the entire array
def std_hig_marks():
    print("\nHighest Marks in the entire array: ")
    hig_marks = np.max(marks)
    print("Heighest Marks in Entire Array: ",hig_marks)
std_hig_marks()

def std_low_marks():
    print("\nLowest Marks in the entire array: ")
    min_marks = np.min(marks)
    print("Lowest Marks In Entire Array: ",min_marks)
std_low_marks()

# Q5. Subject-wise Analysis
# Find the highest marks in each subject.

def std_sub_average():
    hig_sub = np.max(marks, axis = 0)
    print("\nSubject Average: ",hig_sub)
std_sub_average()

def hig_low_subject_avg():
    hig_sub = np.max(marks, axis = 0)
    sub = ["Python","NumPY","Pandas","Java"]
    print("Highest marks of Each Subject: ")
    for data in range(len(sub)):
        print(sub[data],":", hig_sub[data])


    low_sub = np.min(marks, axis = 0)

    sub = ["Python","NumPY","Pandas","Java"]
    print("\nLowest marks of Each Subject: ")
    for data in range(len(sub)):
        print(sub[data],":", low_sub[data])

hig_low_subject_avg()    
  
# Q7. Find Top Student
# Find which student has the highest total marks.
def top_std():
    print("\nTop Students: ")
    top_std = np.argmax(total_marks)
    print("Top Student: ",top_std)
    print("Highest Total: ",np.max(total_marks))
top_std()
# Q8. Find Students Who Scored Above 80
# Use Boolean indexing.

print("\nAbove 80 Scored Students: ")
students = ["student1","student2","student3","student4","student5"]

for i, avg in enumerate(avg_marks):
    if avg >= 80:
        print(f"Student {i+1},({students[i]}): {avg:.2f}")

# Q9. Pass/Fail
# Consider a student PASS if their average is greater than or equal to 50.

print("\nConsider a student PASS if their average is greater than or equal to 50: ")   
pass_fail = np.where(avg_marks >= 50, "Pass","Fail")

for i, data in enumerate(pass_fail, start = 1):
    print(f"Student {i} : {data}")

# Q10. Grade System:
# Assign grades based on average:

print("\nGrade System:")
grade = np.where(
    avg_marks >= 90, "A+",
    np.where(avg_marks >= 80, "A",
             np.where(avg_marks >=70, "B",
                      np.where(avg_marks >= 60, "C",
                               np.where(avg_marks >= 50, "D", "F"),
                               ),
                      ),
             )
    )

for student,(avg, grade) in enumerate(zip(avg_marks, grade), start=1):
    print(f"Student {student}: Average = {avg:.2f} , Grade = {grade}")
'''
