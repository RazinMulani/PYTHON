# Mini Project 2: Identity Matrix Generator using tf.eye()
# 🎯 Objective

# Generate identity matrices of different sizes.

import tensorflow as tf

print("====Identify Matrix Geneartor====")
print("1. Square Identity Matrix")
print("2. Custom Rows and Columns")

choice = int(input("Emter The Choice(1 or 2):"))

if choice == 1:
    size = int(input("Enter Matrix Size:"))
    identity = tf.eye(size)

    print("\nSquare Identity Matrix:")
    print(identity)

if choice == 2:
    rows = int(input("Enter Number Of Rows:"))
    col = int(input("Enter Number Of Column:"))

    identity = tf.eye(
        num_rows=rows,
        num_columns=col
        )
    print("\nCustom Identity Matrix:")
    print(identity)

else:
    print("Invalid Choice!")


