# Initial array to be rotated
arr = [1, 2, 3, 4, 5, 6, 7]

def rotate_arry(arr, k):
    # Loop k times to perform the rotation
    for i in range(k):
        # Remove the last element from the array
        last = arr.pop()
        # Insert the last element at the beginning of the array
        arr.insert(0, last)
    # Return the rotated array
    return arr

# Call the function to rotate the array by 3 positions and print the result
print(rotate_arry(arr, 5))
