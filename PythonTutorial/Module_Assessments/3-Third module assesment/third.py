def main():
    # Step 1: Take the required input from the user
    num = int(input("Enter a number to print prime numbers up to: "))
    
    # Step 2: Loop through all numbers from 2 to num
    for i in range(2, num + 1):
        # Step 3: Check if the current number is prime
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Check divisibility up to sqrt(i)
            if i % j == 0:
                is_prime = False
                break
        
        # Step 4: If the number is prime, print it
        if is_prime:
            print(i)

# Call the main function
main()
