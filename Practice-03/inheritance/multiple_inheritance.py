#example_1
class Mother:
    def cooking(self):
        print("Can cook")

class Father:
    def driving(self):
        print("Can drive")

class Child(Mother, Father):
    pass

c = Child()
c.cooking()  # Output: Can cook
c.driving()  # Output: Can drive

#example_2
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        print("Hello from C")

c = C()
c.greet()  # Output: Hello from C

#example_3
class A:
    def __init__(self):
        print("A initialized")

class B:
    def __init__(self):
        print("B initialized")

class C(A, B):
    def __init__(self):
        super().__init__()  # Calls first parent in MRO
        print("C initialized")

c = C()
# Output:
# A initialized
# C initialized

#example_4
class Father:
    def __init__(self):
        self.father_name = "John"

class Mother:
    def __init__(self):
        self.mother_name = "Jane"

class Child(Father, Mother):
    def show_parents(self):
        print(f"Father: {self.father_name}, Mother: {self.mother_name}")

c = Child()
# Note: mother_name may not be initialized if not called explicitly
c.show_parents()  # Output: Father: John, Mother: AttributeError
