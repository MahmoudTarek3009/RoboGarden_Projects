import random

def insertion_sort(arr):
    # Loop through all elements in the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to insert
        j = i - 1  # The index of the element just before the current one
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key after the last element that is less than it
        arr[j + 1] = key
    
    return arr

def main():
    # Create a random list of numbers
    arr = random.sample(range(1, 101), 10)  # List of 10 random numbers between 1 and 100
    print("Original List:", arr)
    
    # Apply Insertion Sort
    sorted_arr = insertion_sort(arr)
    
    # Print the sorted list
    print("Sorted List:", sorted_arr)

# Call the main function
main()
