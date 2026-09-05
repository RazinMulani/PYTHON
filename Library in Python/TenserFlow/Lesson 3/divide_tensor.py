# tf.divide(): Divides ones tensor by another element by element and returns a new tensor
# Syntax: tf.divide(x, y, name=none)

# Note: Return Value: Returns a new tensor containing the Dividation.

import tensorflow as tf
print("Example 1: Divide Two Numbers (Scalars):\n")
a = tf.constant(200)
b = tf.constant(300)

result = tf.divide(a, b)
print(result)
print("\n=================================================================================")
print("\nExample 2: Divide Two 1-D Tensors:\n")
x = tf.constant([2,3,4])
y = tf.constant([9,0,7]) # inf=infinity
res = tf.divide(x, y)
print(res)

'''x1 =tf.constant([2,3,4])
y1 = tf.constant([6,7])'''  # Get ERROR!
'''res1 = tf.add(x1, y1)
print(res1)''' 
print("\n=================================================================================")
print("\nExample 3: Divide Two 2-D Tensors\n")

x1 = tf.constant([
    [3,4],
    [5,6]
    ])

y1 = tf.constant([
    [7,8],
    [1,2]
    ])

res1 = tf.divide(x1, y1)
print(res1)

print("\n=================================================================================")
print("\nExample 4: Divide Decimal Values\n")

x2 = tf.constant([10.20,40.30])
y2 = tf.constant([30.60,20.56])

print(tf.divide(x2,y2))

print("\n=================================================================================")
print("\nExample 5: Broadcasting\n")

x3 = tf.constant([1,2,3])
y3 = tf.constant(3)

print(tf.divide(x3, y3))
print("\n=================================================================================")

print("\nReal-Life Example\n")
# Suppose a student scored:
# Total Marks = 450
# Subjects = 5

total = tf.constant(450)
subject = tf.constant(5)

average = tf.divide(total, subject)
print("Total Marks:",total)
print("Subjects:",subject)
print("Average:",average)
