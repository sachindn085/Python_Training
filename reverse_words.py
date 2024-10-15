def reverse_words(string):
    # Split the input string into a list of words based on whitespace
    word = string.split()
    
    # Reverse the list of words
    word = word[::-1]
    
    # Join the reversed list of words into a single string with spaces in between
    return ' '.join(word)

# Example input string
string = "hello word"

# Call the function to reverse the words and store the result
result = reverse_words(string)

# Print the result
print(result)  
