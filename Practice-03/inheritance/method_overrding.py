#example_1
#Basic method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # overrides parent method
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks

#example_2
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

#example_3
class Vehicle:
    def __init__(self):
        print("Vehicle created")

class Car(Vehicle):
    def __init__(self):
        print("Car created")  # overrides parent constructor

c = Car()  # Output: Car created

#example_4
class Animal:
    def speak(self):
        print("Animal sound")

class Mammal(Animal):
    def speak(self):
        print("Mammal sound")

class Dog(Mammal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
