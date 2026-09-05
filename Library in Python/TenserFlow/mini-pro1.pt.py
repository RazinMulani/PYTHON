# Mini Project
# Mini Project 1: Student Marks Matrix using tf.constant
# 🎯 Objective

# Store marks of students in a TensorFlow tensor and perform basic operations.

import tensorflow as tf

marks = tf.constant([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
    ])

print("Marks Of Student: ",marks)

print("\nShape: ",marks.shape)

print("\nDtype: ",marks.dtype)

