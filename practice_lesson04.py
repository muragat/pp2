

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # inheritance + super
        self.breed = breed

    def speak(self):   # override
        print("Dog barks")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):   # override
        print("Cat meows")


# 测试
dog1 = Dog("Buddy", 3, "Husky")
cat1 = Cat("Luna", 2, "White")

dog1.speak()
cat1.speak()