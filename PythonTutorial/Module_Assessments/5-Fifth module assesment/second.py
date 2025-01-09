# Define the recursive function for Fibonacci
def fibonacci(n):
    # Base conditions
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive return: sum of previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Main function to test the Fibonacci function
def main():
    # Take input from the user
    n = int(input("Enter the position in the Fibonacci sequence (n): "))
    
    # Call the Fibonacci function and print the result
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")

# Run the program
main()
