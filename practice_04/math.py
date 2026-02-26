#1 Convert degree to radian
import math

# Input degree
degree = 15

# Convert to radian
radian = degree * (math.pi / 180)

# Print result (rounded for required format)
print("Output radian:", round(radian, 6))



#2  Area of a trapezoid
# Given values
height = 5
base1 = 5
base2 = 6

# Calculate area
area = (base1 + base2) / 2 * height

print("Expected Output:", area)



#3 Area of a regular polygon
import math

# Inputs
n = 4        # number of sides
s = 25       # length of side

# Calculate area
area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", int(area))


#4 Area of a parallelogram
# Given values
base = 5
height = 6

# Calculate area
area = base * height

print("Expected Output:", float(area))