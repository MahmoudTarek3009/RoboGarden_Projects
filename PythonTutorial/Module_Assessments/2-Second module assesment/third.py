import math

# Take input from the user and assign it to the variable 'radius'
radius = float(input("Enter the radius of the circle: "))

# Create variables for circumference and area and assign their values
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Print the values of circumference and area
print("Circumference of the circle:", circumference)
print("Area of the circle:", area)
