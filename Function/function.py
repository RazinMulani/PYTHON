# Function In Python: A function is a reusable block of code that perform a specific task.
# Insted of writing the same code multiple time.
# You can define a function once and call it whenever you need it.

# function have two part 1) inbuilt function 2) user define function
# ibuilt function: the fuction alrady exist in pythone programming like print()
# type(),int(),input(),float(),id(),etc..

# User define function: this function create a coder the main part is this function
# 1st user define and then called it whenever they need it.
# --> they have two types 1) Empty function 2) parametrized function

# Empty funtion: using without parameter.
# Example:

def add():
    a=10
    b=20
    c=a+b
    print(c)
add()

# they have so many type to run this program

# 2) direct addition of a+b
def add():
    a=30
    b=40
    print(a+b)
add()

# get value from user
def sub():
    a = int(input("Enter The value of A:"))
    b = int(input("Enter the value of B:"))
    print("Substraction of A and B is:",a-b)
sub()
