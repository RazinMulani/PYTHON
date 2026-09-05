# Mathamatical Operation
# 1) tf.add(): Used To perform Elements-Wise Addition Betwwen Two Tensors.
# Syntax : tf.add(x, y, name=none)

# Note: Return Value: Returns a new tensor containing the sum.

import tensorflow as tf
print("Example 1: Add Two Numbers (Scalars):\n")
a = tf.constant(200)
b = tf.constant(300)

result = tf.add(a, b)
print(result)
print("\n=================================================================================")
print("\nExample 2: Add Two 1-D Tensors:\n")
x = tf.constant([2,3,4])
y = tf.constant([9,8,7])
res = tf.add(x, y)
print(res)

'''x1 =tf.constant([2,3,4])
y1 = tf.constant([6,7])'''  # Get ERROR!
'''res1 = tf.add(x1, y1)
print(res1)''' 
print("\n=================================================================================")
print("\nExample 3: Add Two 2-D Tensors\n")

x1 = tf.constant([
    [3,4],
    [5,6]
    ])

y1 = tf.constant([
    [7,8],
    [1,2]
    ])

res1 = tf.add(x1, y1)
print(res1)

print("\n=================================================================================")
print("\nExample 4: Add Decimal Values\n")

x2 = tf.constant([10.20,40.30])
y2 = tf.constant([30.60,20.56])

print(tf.add(x2,y2))

print("\n=================================================================================")
print("\nExample 5: Broadcasting\n")

x3 = tf.constant([1,2,3])
y3 = tf.constant(3)

print(tf.add(x3, y3))
print("\n=================================================================================")

print("\nReal-Life Example\n")

# Suppose you have two months' sales.
# January:[1000, 2000, 3000]
# February:[500, 700, 800]

sales1 = tf.constant([1000, 2000, 3000])
sales2 = tf.constant([500, 700, 800])

total =tf.add(sales1, sales2)
print("Total Months sales of January & February: ",total)
