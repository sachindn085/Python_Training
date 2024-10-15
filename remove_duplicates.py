def r_d(l):
    # Sort the list in ascending order
    l.sort()
    n=len(l)  
    # Iterate through the list, stopping before the last two elements
    for i in range(len(l) - 2):
        # Check if the current element is equal to the element two positions ahead  
        while l[i] == l[i + 2]:  
            # Remove the duplicate element
            l.remove(l[i]) 
            if l[i]=="_":
                break 
            # Append a placeholder to maintain list length
            l.append("_") 
        
    while len(l)<n:
        l.append("_") 
            
    return l  # Return the modified list

# Input list with duplicates
list1 = [0, 1, 1, 1, 2, 2, 3, 3, 3,3]
# Call the function to remove excess duplicates
op = r_d(list1)
# Print the modified list with duplicates removed
print(f"Removed sorted duplicate list {op}")