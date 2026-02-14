#example_1
#Simple class and object
# Define a simple class
class Person:
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

# Create an object
p1 = Person("Alice", 20)

print(p1.name, p1.age)  # Output: Alice 20

#example_2
#Class with a method
# Class with behavior (method)
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} is barking"

# Object
d = Dog("Buddy")
print(d.bark())  # Output: Buddy is barking

#example_3
#Class with default values
# Default value in constructor
class Car:
    def __init__(self, brand, year=2024):
        self.brand = brand
        self.year = year

c1 = Car("Toyota")
print(c1.year)  # Output: 2024

#example_4
#Class with class variable
# Class variable shared by all objects
class Student:
    school = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Tom")
s2 = Student("Jerry")

print(s1.school)  # Output: ABC School
print(s2.school)
