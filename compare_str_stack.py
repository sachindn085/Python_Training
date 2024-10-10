# Lists of opening and closing brackets
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

# Function to check if brackets in a string are balanced
def check(myStr):
    # Initialize an empty stack to keep track of opening brackets
    stack = []  
    # Iterate through each character in the input string
    for i in myStr:
        # If the character is an opening bracket, push it onto the stack
        if i in open_list:
            stack.append(i)
        # If the character is a closing bracket
        elif i in close_list:
            # Find the position of the closing bracket in the close_list
            pos = close_list.index(i)
            # Check if there is a corresponding opening bracket on the stack
            if (len(stack) > 0) and (open_list[pos] == stack[len(stack) - 1]):
                # Pop the matching opening bracket from the stack
                stack.pop()  
            else:
                # Return "Unbalanced" if no match is found
                return "Unbalanced"  
    # After processing all characters, check if the stack is empty
    if len(stack) == 0:
        # Return "Balanced" if all brackets matched
        return "Balanced"  
    else:
        # Return "Unbalanced" if there are unmatched brackets
        return "Unbalanced"  

# Input string containing brackets
string = "{[]{()}}"
# Print the result of the check function
print(string, "-", check(string))
