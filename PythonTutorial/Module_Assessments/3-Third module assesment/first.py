def main():
    # Step 1: Define the required variables
    num_terms = int(input("Enter the number of terms you want in the Fibonacci sequence: "))
    
    # Step 2: Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Step 3: Generate and print the Fibonacci sequence
    for i in range(num_terms):
        print(a)  # Print the current Fibonacci number
        a, b = b, a + b  # Update the Fibonacci numbers

# Call the main function to start the program
main()
