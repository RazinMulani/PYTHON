# Returning Function: Is a function that gives back a value using the return keyword
'''
def sub(a,b):
    c =a - b
    return c
result =sub(60,60)
print("Substraction of A And B:",result)
'''
# Returning Multiple Values From A Function
'''
def arithmatic_ope(a,b):
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b

    return add, sub, mult, div

x,y,z,w = arithmatic_ope(100,20)
print("Add is: ",x)
print("Sub is: ",y)
print("Mult is: ",z)
print("Div is: ",w)
'''
# 4) Create a function calculate_grade(marks) that accepts marks as a parameter and returns the grade:

# 90–100 → A, 75–89 → B, 60–74 → C, 40–59 → D, Below 40 → Fail

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "False"

marks = int(input("Enter The Students Marks:"))

grade = calculate_grade(marks)
print("Grade: ",grade)
