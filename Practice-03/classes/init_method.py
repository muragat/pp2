#example_1
#Create a class named Person, use the __init__() method to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#example_2
#Create a Person class with multiple parameters:
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#example_3
#Default values in constructor
# Default value in __init__
class Car:
    def __init__(self, brand, year=2023):
        self.brand = brand
        self.year = year

c1 = Car("Toyota")
c2 = Car("BMW", 2020)

print(c1.year)  # 2023
print(c2.year)  # 2020
 

#example_4
#Constructor + method
# Using __init__ with another method
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount("Alice", 1000)
account.deposit(500)

print(account.balance)  # Output: 1500
