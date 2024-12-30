# Get user inputs
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform calculations and store results in variables
sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number

# Handle division with check for zero
if second_number != 0:
    division_result = first_number / second_number
else:
    division_result = "Error! Division by zero."

# Print the results
print("Sum:", sum_result)
print("Subtraction:", subtraction_result)
print("Multiplication:", multiplication_result)
print("Division:", division_result)
