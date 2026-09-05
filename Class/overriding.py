# Method Oveerriding:
# Method Overriding Occures When a chiled class defiene a method with the same name asa method in
# its parents class but provides its own implementation

# Example:

class Animal:
    def sound(self):
        print("Animal makes a Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Sound Is Bhoow..!")

class Cat(Animal):
    def sound(self):
        print("Cats Sound Is Meoww..!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()



# Practice Question 1
'''
class Animal():
    def sound(self,a_sound):
        print("Animal Makes:",a_sound)

class Dog(Animal):
    def sound(self,a_sound):
        self.a_sound = a_sound
        print("Dog makes:",self.a_sound)

class Cat(Animal):
    def sound(self,a_sound):
        self.a_sound = a_sound
        print("Cat Makes:",self.a_sound)

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound("Some Sound")
dog.sound("barks")
cat.sound("meow")
'''

# Practice Question 2
'''
class Vehicle:
    def start(self):
        print("How to start Vehicle car/bike?:")

class Car(Vehicle):
    def start(self):
        print("Car Start With A Key")

class Bike(Vehicle):
    def start(self):
        print("Bike Start With A Button")


vehicle = Vehicle()
car = Car()
bike = Bike()

vehicle.start()
car.start()
bike.start()
'''

# Practice Question 3
'''
class Employee:
    def __init__(self):
        self.f_t_s = 50000
        self.p_t_s = 25000
        
    def calculate_salary(self):
        print("Employe Salary:")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full Time Employee Salary:",self.f_t_s)

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part Time Employee Salary:",self.p_t_s)

emp = Employee()
fts = FullTimeEmployee()
pts = PartTimeEmployee()

emp.calculate_salary()
fts.calculate_salary()
pts.calculate_salary()
'''
# Practice Question 4






