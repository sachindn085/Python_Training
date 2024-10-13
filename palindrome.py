def palindrome(s):
    # Initialize an empty string to store alphanumeric characters
    a = ""
    
    # Iterate through each character in the input string
    for i in s:
        # Check if the character is alphanumeric (letters and numbers)
        if i.isalnum():
             # Append the character to the new string
            a += i 
    
    # Check if the cleaned string is the same forwards and backwards
    if a == a[::-1]:
        # Return "True" if it's a palindrome
        return "True"  
    else:
        # Return "False" if it's not a palindrome
        return "False"  
# Example input string
s1 = "malay''''aam"
# Call the function to check if the string is a palindrome
b = palindrome(s1)
# Print the result
print(b)  