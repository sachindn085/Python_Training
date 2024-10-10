# Input string containing brackets
s = "{[()}"

# Tuples of adjacent matching brackets
adj = ("{}", "[]", "()")

# Function to check if the brackets are balanced
def abc(a):
    # Initialize an iteration counter
    i = 0  
    # Continue until there are no characters left
    while len(a) > 0: 
        # Increment the iteration counter
        i += 1  
        # If the string has only one character or if iterations exceed the string length, return "False"
        if len(a) == 1 or i > len(a):
            return "False"
        # Replace matching adjacent brackets with an empty string
        for j in adj:
            # Remove matching brackets from the string
            a = a.replace(j, "")  
    # If all brackets are matched and removed, return "True"
    return "True"

# Call the function and store the result
str1 = abc(s)

# Print the result indicating whether the brackets are balanced
print(str1)
