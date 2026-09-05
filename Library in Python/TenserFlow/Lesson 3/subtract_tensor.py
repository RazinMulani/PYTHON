# tf.subtract: subtracts one tensor from another element by element.
# Syntax: tf.subtract(x, y, name=none)

# Note: Return Value: Returns a new tensor containing the Subtraction.

import tensorflow as tf
print("Example 1: Subtract Two Numbers (Scalars):\n")
a = tf.constant(200)
b = tf.constant(300)

result = tf.subtract(a, b)
print(result)
print("\n=================================================================================")
print("\nExample 2: Subtract Two 1-D Tensors:\n")
x = tf.constant([2,3,4])
y = tf.constant([9,8,7])
res = tf.subtract(x, y)
print(res)

'''x1 =tf.constant([2,3,4])
y1 = tf.constant([6,7])'''  # Get ERROR!
'''res1 = tf.add(x1, y1)
print(res1)''' 
print("\n=================================================================================")
print("\nExample 3: Subtract Two 2-D Tensors\n")

x1 = tf.constant([
    [3,4],
    [5,6]
    ])

y1 = tf.constant([
    [7,8],
    [1,2]
    ])

res1 = tf.subtract(x1, y1)
print(res1)

print("\n=================================================================================")
print("\nExample 4: Subtract Decimal Values\n")

x2 = tf.constant([10.20,40.30])
y2 = tf.constant([30.60,20.56])

print(tf.subtract(x2,y2))

print("\n=================================================================================")
print("\nExample 5: Broadcasting\n")

x3 = tf.constant([1,2,3])
y3 = tf.constant(3)

print(tf.subtract(x3, y3))
print("\n=================================================================================")

print("\nReal-Life Example\n")
# Suppose you scored:
# Total Marks = 500
# Obtained Marks = 425

total = tf.constant(500)
obtained = tf.constant(425)

result = tf.subtract(total, obtained)
print("Total Marks Is:",total)
print("Obtain Marks Of Student:",obtained)
print("Result:",result)

