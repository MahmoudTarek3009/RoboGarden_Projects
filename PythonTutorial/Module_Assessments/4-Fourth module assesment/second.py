import random

# Function to merge two halves of the list
def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    # Add remaining elements from both halves if any
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Function to implement the merge sort algorithm
def merge_sort(arr):
    # Base case: if the list has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Sort the left half
    right_half = merge_sort(arr[mid:])  # Sort the right half

    # Merge the sorted halves
    return merge(left_half, right_half)

def main():
    # Create a random list of 10 numbers between 1 and 100
    random_list = random.sample(range(1, 101), 10)
    print("Original list:", random_list)
    
    # Sort the list using merge sort
    sorted_list = merge_sort(random_list)
    
    # Print the sorted list
    print("Sorted list:", sorted_list)

# Run the main function
if __name__ == "__main__":
    main()
