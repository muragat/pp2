#example_1
#Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#Example_2
#Sort strings by length:
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#Example_3
#Sort a list of numbers (ascending)
# List of numbers
nums = [5, 2, 9, 1, 7]

# Default sorting is ascending
sorted_nums = sorted(nums)

print(sorted_nums)  # Output: [1, 2, 5, 7, 9]

#Example_4
#Sort a list of numbers (descending)
# Sort in reverse order
nums = [5, 2, 9, 1, 7]

sorted_desc = sorted(nums, reverse=True)

print(sorted_desc)  # Output: [9, 7, 5, 2, 1]
