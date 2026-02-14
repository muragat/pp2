#example_1
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # call parent method
        print("Hello from Child")

c = Child()
c.greet()
# Output:
# Hello from Parent
# Hello from Child

#example_2
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created: {self.name}")

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)  # call Person's constructor
        self.major = major
        print(f"Student created: {self.name}, Major: {self.major}")

s = Student("Alice", "IT")

#example_3
class Animal:
    def __init__(self):
        print("Animal created")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal created")

class Dog(Mammal):
    def __init__(self):
        super().__init__()
        print("Dog created")

d = Dog()
# Output:
# Animal created
# Mammal created
# Dog created

#exaple_4
class A:
    def display(self):
        print("Display from A")

class B(A):
    def display(self):
        print("Display from B")
        super().display()  # call A's display

b = B()
b.display()
# Output:
# Display from B
# Display from A

