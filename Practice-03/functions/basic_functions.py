#Example_1
# This is a function definition
def my_function():
  print("Hello from a function")

my_function()

#Example_2
#You can call the same function multiple times:
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#Example_3
#With functions we can convert temperatures from Fahrenheit to Celsius:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#Example_4
#with functions we can calculate the area of a circle given its radius:
def radius_to_area(radius):
  return 3.14 * radius ** 2
print(radius_to_area(5))
