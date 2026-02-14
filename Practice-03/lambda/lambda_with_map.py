#example_1
#Double all numbers in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#Example_2
#Square each number in a list
# List of numbers
nums = [2, 4, 6, 8]

# map applies a function to each element
squares = list(map(lambda x: x ** 2, nums))

print(squares)  # Output: [4, 16, 36, 64]

#Example_3
#Get the length of each word
# List of words
words = ["python", "map", "function"]

# map finds the length of each word
lengths = list(map(len, words))

print(lengths)  # Output: [6, 3, 8]

#Example_4
#Convert temperatures from Celsius to Fahrenheit
# List of temperatures in Celsius
celsius = [0, 10, 20, 30, 40]

# Formula: Fahrenheit = (C × 9/5) + 32
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]
