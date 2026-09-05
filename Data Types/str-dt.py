# text Data type: For the text we use str means string datatype
# string is used for store text or seqence of characters like 'a', 'name', etc..
# we can create string using single(''), duble(" ") and tripal(''' ''') quotes.
'''
# using single quotes:
str1 = 'Razin'
print(str1)

# using double quotes:
str2 = " Rafik "
print(str2)

# using triple quotes:
str3 = 'mulani'
print(str3)

# indexing: U gate any perticular value for helping of indexing
# idexing have two types 1's is positive idexing and 2'nd is negative indexing
# positive indexing always strat from '0'

V = "Mango"
print(V[0]) # M
print(V[1]) # a
print(V[2]) # n
print(V[3]) # g
print(V[4]) # o

# negative indexing always start from '-1'

V = "Mango"
print(V[-1]) # o
print(V[-2]) # g
print(V[-3]) # n
print(V[-4]) # a
print(V[-5]) # M

#U dont change value like a list becouse of string is a immutable 

V[0] = 'R'
print(V)
'''
# slicing: slicing means you get perticular part in a string
# synatx: string[start : end] --> you should put where slicing start value and end value
# alwys tek End point n-1 --> string[n:n-1]
S = "Banana"
S = S[2:6]
print(S)
