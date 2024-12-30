def calc_average(ls):
    # Calculate the sum of the list
    total_sum = sum(ls)
    
    # Calculate the length of the list
    length = len(ls)
    
    # Check if the list is not empty to avoid division by zero
    if length == 0:
        return "The list is empty, cannot calculate average."
    
    # Calculate and return the average
    average = total_sum / length
    return average

def main():
    # Example list of numbers
    ls = [12, 70, -4, 16, 22]
    
    # Call the function to calculate the average
    result = calc_average(ls)
    
    # Print the result
    print(f"The average of the list is: {result}")
    
    return result

# Run the main function
main()
