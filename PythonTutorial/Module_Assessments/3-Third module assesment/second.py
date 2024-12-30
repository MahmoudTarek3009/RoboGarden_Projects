def main():
    # Step 1: Take the required input from the user
    num = int(input("Enter a number to calculate its factorial: "))
    
    # Step 2: Initialize a variable to store the factorial result
    factorial = 1
    
    # Step 3: Start the loop and apply the factorial algorithm
    for i in range(1, num + 1):  # Loop from 1 to the number
        factorial *= i  # Multiply factorial by the current number
    
    # Step 4: Print the factorial
    print(f"The factorial of {num} is {factorial}")

# Call the main function
main()
