def major_element(l):
    # Initialize an empty dictionary to count occurrences of each element
    c_dict = {}
    
    # Iterate through each element in the list
    for i in l:
        # If the element is not already a key in the dictionary, count its occurrences
        if i not in c_dict.keys():
            # Count how many times 'i' appears in the list
            c_dict[i] = l.count(i)  
    
    # Create a list of the counts of each element
    l1 = list(c_dict.values())
    l2 = []  # Initialize an empty list to store the major elements
    
    # Iterate through the dictionary to find elements with the maximum count
    for k, v in c_dict.items():
        # Check if the current count is the maximum
        if max(l1) == v:  
             # Add the element to the list of major elements
            l2.append(k) 
    # Return the list of major elements
    return l2  

# Example list of integers
main_l = [2, 1, 2, 3, 2, 1, 1]
# Call the function to find major elements
op = major_element(main_l)
# Print the result
print(op)  
