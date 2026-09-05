# tf.multiply(): Multiplication of two tensor element by element and returns a new tensor
# Syntax: tf.multipal(x, y, name=none)

# Note: Return Value: Returns a new tensor containing the Multiplication.

import tensorflow as tf
print("Example 1: Multipal Two Numbers (Scalars):\n")
a = tf.constant(200)
b = tf.constant(300)

result = tf.multiply(a, b)
print(result)
print("\n=================================================================================")
print("\nExample 2: Multipal Two 1-D Tensors:\n")
x = tf.constant([2,3,4])
y = tf.constant([9,8,7])
res = tf.multiply(x, y)
print(res)

'''x1 =tf.constant([2,3,4])
y1 = tf.constant([6,7])'''  # Get ERROR!
'''res1 = tf.add(x1, y1)
print(res1)''' 
print("\n=================================================================================")
print("\nExample 3: Multipal Two 2-D Tensors\n")

x1 = tf.constant([
    [3,4],
    [5,6]
    ])

y1 = tf.constant([
    [7,8],
    [1,2]
    ])

res1 = tf.multiply(x1, y1)
print(res1)

print("\n=================================================================================")
print("\nExample 4: Multipal Decimal Values\n")

x2 = tf.constant([10.20,40.30])
y2 = tf.constant([30.60,20.56])

print(tf.multiply(x2,y2))

print("\n=================================================================================")
print("\nExample 5: Broadcasting\n")

x3 = tf.constant([1,2,3])
y3 = tf.constant(3)

print(tf.multiply(x3, y3))
print("\n=================================================================================")

print("\nReal-Life Example\n")
# Suppose a shop sells:
# Price = ₹500
# Quantity = 4
price = tf.constant(500)
quantity = tf.constant(4)

result = tf.multiply(price, quantity)
print("Price Of Product:",price)
print("Quantity Of Product:",quantity)
print("Total Amount:",result)
