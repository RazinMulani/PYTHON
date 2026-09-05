# Pandas Series?

# Pandas Series are homogeneous one-dimensional objects that all data are same type and data are same type
# and are implicit labeeled wit an index

# Pandas:
# Random Python pandas series of numbers

import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'])
print(s,"\n")

# Lets Create Pandas Series From Dictionary

dict = pd.Series({
    'a':1,
    'b':2,
    'c':3
    })
print(dict)

# Simple operation on pandas series: When we have python pandas series, we can perform several simple
# operation
# 1. Dictionary
# 2. Array

print("\nDictionary")
dictionary = {'a':1,'b':2,'c':3}
s1 = pd.Series(dictionary)
print(s1)

print("\nArray:")
array = [1,2,3]
s2 = pd.Series(array)
print(s2)

print("\nImport Excel File or Read File\n")
# Create Excel File and read the file
df = pd.read_csv("student.csv")
print(df)

print("\n",df["roll"].values)
print("\n",df["name"].values)
print("\n",df["location"].values)
