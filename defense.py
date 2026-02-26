class Animal:
    def __init__(self, name, age): self.name, self.age = name, age

class Dog(Animal):
    def info(self): print(f"Dog {self.name}, Age {self.age}, Sound: Woof!")

class Cat(Animal):
    def info(self): print(f"Cat {self.name}, Age {self.age}, Sound: Meo!")

animals = [Dog("Buddy",3), Cat("Luna",2), Dog("Max",5)]
for a in sorted(animals, key=lambda x: x.age): a.info()