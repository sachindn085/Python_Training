# Initialize a list of numbers
a = [2, 3, 4, 6, 8, 1]

# Outer loop to iterate through each element in the list
for i in range(0, len(a)):
    # Inner loop to compare the current element with the remaining elements
    for j in range(i + 1, len(a)):
        # If the current element is greater than or equal to the next element
        if a[i] >= a[j]:
            # Swap the elements to sort the list
            a[i], a[j] = a[j], a[i]

# Print the sorted list
print(a)
