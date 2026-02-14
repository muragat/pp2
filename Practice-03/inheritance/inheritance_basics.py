#example_1
# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    pass  # No new methods, inherits everything

d = Dog()
d.speak()  # Output: Animal makes a sound

#example_2
#Adding new methods in child class
# Parent class
class Vehicle:
    def start(self):
        print("Vehicle started")

# Child class
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()  # inherited
c.drive()  # new method

#example_3
# Parent class
class Animal:
    def speak(self):
        print("Animal sound")

# Child overrides the method
class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()  # Output: Meow

#example_4
# Parent class
class Person:
    def __init__(self, name):
        self.name = name

# Child class
class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)  # call parent constructor
        self.major = major

s = Student("Alice", "IT")
print(s.name, s.major)
