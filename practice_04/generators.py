#1 Generator that generates squares up to N
# Generator function to produce squares from 1 to N
def generate_squares(n):
    for i in range(1, n + 1):
        yield i * i   # yield returns value one by one instead of storing all

# Test
N = 5
for square in generate_squares(N):
    print(square)




#2 Generator to print even numbers (comma separated)
# Generator for even numbers from 0 to n
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

# Input from console
n = int(input("Enter a number: "))

# Convert generator output to comma-separated string
print(",".join(str(num) for num in even_numbers(n)))



#3 Generator for numbers divisible by 3 and 4
# Generator for numbers divisible by both 3 and 4
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Test
n = 50
for num in divisible_by_3_and_4(n):
    print(num)



#4 Generator squares(a, b) and test with for loop
# Generator to yield squares between a and b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Test
for value in squares(3, 7):
    print(value)


#5 Generator that returns numbers from n down to 0
# Generator for countdown from n to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test
for num in countdown(5):
    print(num)