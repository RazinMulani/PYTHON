#Practice Pandas And Numpy

# Create DataFrame
import pandas as pd
import numpy as np

marks = np.array([
    [78, 85, 69],
    [65, 72, 80],
    [92, 88, 95],
    [45, 55, 48],
    [81, 79, 85]
    ])

students = ["Amit","Razin","Rahul","Sanika","Mansi"]
df = pd.DataFrame(
    marks,
    index = students,
    columns = ["Python","NumPY","Pandas"]
    )
print(df)
print("\n===================================================================\n")

# Q1. Using Pandas, find the average marks of each student.

df["Average"] = df.mean(axis=1)
print(df["Average"])

      
