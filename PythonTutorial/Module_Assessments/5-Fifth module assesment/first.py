def factorial(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

def main():
    # Take user input for the number
    num = int(input("Enter a number to calculate its factorial: "))
    
    # Call the factorial function
    result = factorial(num)
    
    # Print the result
    print(f"The factorial of {num} is: {result}")

# Run the main function
main()
