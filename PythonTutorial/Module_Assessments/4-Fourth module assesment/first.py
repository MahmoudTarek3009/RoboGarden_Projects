import random

def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop for each pass
    for i in range(n):
        # Flag to optimize the algorithm (if no swaps, the list is sorted)
        swapped = False
        
        # Inner loop to compare adjacent elements
        for j in range(0, n-i-1):  # We reduce the range with each pass
            if arr[j] > arr[j+1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, the list is sorted
        if not swapped:
            break
    
    return arr

def main():
    # Step 1: Generate a random list of numbers
    arr = random.sample(range(1, 101), 10)  # List of 10 unique random numbers from 1 to 100
    print("Original List:", arr)
    
    # Step 2: Apply the Bubble Sort algorithm
    sorted_arr = bubble_sort(arr)
    
    # Step 3: Print the sorted list
    print("Sorted List:", sorted_arr)

# Call the main function to execute the program
main()
