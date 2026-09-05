# tf.reduce_sum(): Adds all values in tenxor and return their totals:
# Syntax: tf.reduce(input_tensor, axis=none, keepdim=False, name=none)
# Why is it called "Reduce"?
# The word reduce means to decrease the dimensions of a tensor by combining multiple values
# into fewer values

import tensorflow as tf
print("Example 1: Sum of All Elements:\n")

x = tf.constant([10,20,30,40])
result = tf.reduce_sum(x)
print(result)

print("\n==============================================================================\n")

print("Example 2: Sum of a 2-D Tensor\n")
x1 = tf.constant([
    [10,20],
    [30,40]
    ])

print(tf.reduce_sum(x1))
