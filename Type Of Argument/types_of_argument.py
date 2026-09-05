# What is the meaning of argument in Python?
# --> In Python, an argument is a value that you pass in a fuction when you call it

# Types Of Argument
# There are Four types in Argument
#1) positional argument
#2) keyword argument
#3) default argument
#4) variable argument
'''
#1) Positional Argument:-
#--> In the positional argument, value are passed in the same order as they are define in the function
# Example 1:

def add(a,b,c):
    print("Addition is:", a+b+c)

add(10,20,30) # Addition is: 60

# Example 2:

def student(name,age):
    print("name",name)
    print("age",age)

student("razin",22)

'''

# 2) Keyword of Argument:
'''
# --> In keyword arguments, you specify the parameter name while passing the value
# Example 2:

def sub(a,b,c):
    print("Substraction is: ",a-b-c)

sub(a=40,b=20,c=10)
'''






