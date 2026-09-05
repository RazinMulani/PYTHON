# Parameterized function: A parameterized function is a function take parameter(inputs)a perform a task.
# Paramteres is variable written inside the paranthesis of a function definition.

# you write one code so many different different types
'''
# 1)
def add(a,b):
    c = a+b
    print(c)
add(10,20)

# 2)
def add(a,b):
    print(a+b)
add(45,10)

# 3) get value from user

def add(a,b):
    print(a+b)
x = int(input("Enter The value of x:"))
y = int(input("Enter The value of y:"))
add(x,y)
'''
# 4)Create a function calculate_area(length, width) that accepts length and width as parameters and returns the area
# of a rectangle.
'''
def calculate_area(l,w):
    print("Aria: ",l*w)
a = int(input("Enter Length: "))
b = int(input("Enter Width: "))
calculate_area(a,b)
'''

# Create a function calculate_grade(marks) that accepts marks as a parameter and print the grade:

# 90–100 → A, 75–89 → B, 60–74 → C, 40–59 → D, Below 40 → Fail
def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        print("A")
    elif marks >= 75 and marks <=89:
        print("B")
    elif marks >= 60 and marks <= 74:
        print("C")
    elif marks >= 40 and marks <= 59:
        print("D")
    elif marks <= 40:
        print("Fail")

x = int(input("Enter The Student Marks: "))
calculate_grade(x)
