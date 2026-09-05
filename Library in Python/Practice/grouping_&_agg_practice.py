# Grouping and Aggregation(agg())

import pandas as pd

data = {
    "Department": ["HR", "IT", "HR", "IT", "Sales", "Sales", "IT", "HR"],
    "Employee": ["Amit", "Raj", "Priya", "Neha", "Karan", "Pooja", "John", "Riya"],
    "Salary": [30000, 50000, 35000, 60000, 45000, 40000, 70000, 32000],
    "Experience": [2, 5, 3, 6, 4, 2, 7, 1],
    "Gender": ["M", "M", "F", "F", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)

print(df)
print("\n====================================================================\n")

print("Beginner Level Questions:")
# Q1) Desplay All Departments

print("Desplay All Departments")
print(df["Department"])

print("\n====================================================================\n")

# Q2) Group the data by Department.
print("Group The Data By Department")

grouped = df.groupby("Department")


for department, group in grouped:
    print("\nDEPARTMENT",department)
    print(group)

print("\n====================================================================\n")

# Q3) Find the total salary of each department.
print("The Total Salary Of Each Department")
print(df.groupby("Department")["Salary"].sum())

print("\n====================================================================\n")

# Q4) Find the average salary of each department.
print("The Average Salary Of Each Department")
print(df.groupby("Department")["Salary"].mean())

print("\n====================================================================\n")
# Q5) Find the maximum salary in each department.
print("Maximum Salary In Each Department.")
print(df.groupby("Department")["Salary"].max())

print("\n====================================================================\n")
# Q6) Find the minimum salary in each department.
print("Minimum Salary In Each Department.")
print(df.groupby("Department")["Salary"].min())

print("\n====================================================================\n")
# Q7) Count the number of employees in each department.
print("Number of Employe in Each Department.")
print(df.groupby("Department")["Employee"].count())

print("\n====================================================================\n")
# Q8) Find the average experience of employees department-wise.
print("The Average Experience Of Employees Department-Wise.")
print(df.groupby("Department")["Experience"].mean())

print("\n====================================================================\n")

print("Intermediate Level Questions:")
# Q9) Find both minimum and maximum salary for each department.
print("Minimum and Maximumm Salary For Each Department:")
print(df.groupby("Department")["Salary"].agg(["min","max"]))

print("\n====================================================================\n")

# Q10) Find the sum and mean of Salary department-wise.
print("Sum and Mean of Salary Department-Wise.")
print(df.groupby("Department")["Salary"].agg(["sum","mean"]))

print("\n====================================================================\n")

# Q11) Group by Gender and calculate the average salary.
print("Group by Gender and calculation the average salary.")
print(df.groupby("Gender")["Salary"].mean())

print("\n====================================================================\n")

# Q12) Group by Department and Gender together.
print("Group by Department and Gendet together.")

grouped = df.groupby(["Department","Gender"])

for (department,gender), group in grouped:
    print(f"\n Department {department} & Gender {gender}")
    print(group)

print("\n====================================================================\n")

# Q13) Find the highest-paid employee in each department.
print("Find The Heighest -paid employee in each department")

result = df.loc[df.groupby("Department")["Salary"].idxmax()] # idxmax: it is find heighest paid employee 
print(result)

print("\n====================================================================\n")

# Q14) Find the total experience of employees in each department.

print("Total Experience of employees in each department.")

print(df.groupby("Department")["Experience"].sum())

print("\n====================================================================\n")

# Q15) Sort departments based on their average salary (highest first).

print("Sort Departments Based on Their Average Salary(highest first)")

result = df.groupby("Department")["Salary"].agg(["mean","max"])
print(result)
print("\n Heighst First\n")
result1 = df.groupby("Department")["Salary"].mean().sort_values(ascending = False).round(2)
print(result1)

# Q16) Use .agg() to display: Total Salary, Average Salary, Maximum Salary, Minimum Salary,Employee Count
# for every department.

print("\n====================================================================\n")
print("Total Salary, Average Salary, Max and Min, Employee Count Perform at Once.")

agg_result = df.groupby(["Department","Employee"])["Salary"].agg(['sum','mean','max','min','count'])
print(agg_result)


