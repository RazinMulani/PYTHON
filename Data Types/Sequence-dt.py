# Seqence Data Type: A sequence data type in pythone is collection of multiple item  arranged in an order, where each item can be using its index number
# they have three types in Sequence data type
# 1) list  2) Tuple  3) range

# 1) List: store multiple item using of [] squere brackets they have store any type of data
# - list access multiple values
# - list is redable and writable, list is mutable also
# example:
'''
list1 = [10,'razin',25.5,True,3j,10]
print(list1)

# Positive indexing: Positive indexing always start from '0'
print(" Positive Indexing")
print(list1[0]) # 10
print(list1[1]) # razin
print(list1[2]) # 25.5
print(list1[3]) # True
print(list1[4]) # 3j
print(list1[5]) # 10

# Negative Inedexing: Negative indexing start from -1

print("Negative Indexing")
print(list1[-1]) # 10
print(list1[-2]) # razin
print(list1[-3]) # 25.5
print(list1[-4]) # True
print(list1[-5]) # 3j
print(list1[-6]) # 
# mutable list Example:

list1[0] = 20
print(list1) # [20, 'razin', 25.5, True, 3j, 10]
print("Change the first element of list

# list also support slicing
# syntax of slicing: variable[start : end] 

print(list1[1:4]) # o/p: ['razin', 25.5, 

# 2) Tuple: Tuple also store multiple values but tuple is immutable and it is only redable not writable
# --> Tuple also get dublicate values
t = (10,'razin',25.5,True,3j,10)
print(t)


# immutable Example:

t[0]=20
print(t) ## show type Error
'''
# 3) Range: Range is nothing but he built-in function, and it is used genrate
#    of sequence of number, Mostly range used in loops
# --> range() does not get the last number or element

#Example:
'''
r = range(10)
for i in r:
    print(i)

#o/p:
0
1
2
3
4
5
6
7
8
9
'''
'''
# U call the function Directly
# Example:

for i in range(1,10):
    print(i)

o/p:
1
2
3
4
5
6
7
8
9
'''
'''
# using step:
# --> syntax: range(start,stop,step)

# wap get range 1 to 10 with no. of 2 steps.

for i in range(1,10,2):
    print(i)

o/p:
1
3
5
7
9
'''












