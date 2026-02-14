#example_1
#Filter even numbers
# List of numbers
nums = [1, 2, 3, 4, 5, 6]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

print(evens)  # Output: [2, 4, 6]

#Example_2
#Filter positive numbers
# List with positive and negative values
numbers = [-5, 3, -1, 7, 0, 2]

# Keep only positive numbers
positives = list(filter(lambda x: x > 0, numbers))

print(positives)  # Output: [3, 7, 2]

#Example_3
#Filter words longer than 5 characters
# List of words
words = ["apple", "banana", "cat", "elephant", "dog"]

# Keep words with length greater than 5
long_words = list(filter(lambda w: len(w) > 5, words))

print(long_words)  # Output: ['banana', 'elephant']

#Example_4
#Remove empty strings from a list
# List containing empty and non-empty strings
data = ["hello", "", "world", "", "python"]

# bool returns False for empty strings, so they get filtered out
clean_data = list(filter(bool, data))

print(clean_data)  # Output: ['hello', 'world', 'python']
