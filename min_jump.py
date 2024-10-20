def jump(l):
    # Start from the second element (index 1)
    i=1  
    # Initialize the count of jumps
    count=1 
    # Continue until the index exceeds the length of the list 
    while i<len(l):  
        #print(l[i])  # Uncomment to see the current jump value
        # Check if the jump exceeds the bounds of the list
        if i+l[i]>len(l)-1: 
            # Return False if jump is not possible 
            return False  
        # If the current jump value is 0, can't proceed
        elif l[i]==0:  
            # Return False if jump is not possible
            return False  
        # Move to the next index based on the jump value
        i+=l[i]  
        # Increment the count of jumps
        count+=1  
        # Check if we have reached the last index
        if i==len(l)-1:  
             # Return the total number of jumps
            return count 
# Example list of jump values
l1=[2,2,1,2,4]  
# Call the jump function with the list
op=jump(l1)  
# Check if the jump was successful
if op==False:  
     # Output if jump isn't possible
    print(f"The jump is not possible") 
else:
     # Output the number of jumps
    print(f"The jump steps are {op}")
