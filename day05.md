# Day 5 :

## 1.Python Program to Compute Factorial of a Number

The code defines a recursive function to calculate the factorial of a non-negative integer. It prompts the user for input, checks if the input is negative or zero, and then computes and displays the factorial for positive integers using the recursive fact function.

```python
def factorial(n):
    #  if n is 0, return 1 
    if n == 0:
        return 1
    else:
        # return n multiplied by the factorial of (n-1)
        return n * factorial(n - 1)

# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter a number: "))

# Check if the entered number is negative
if num < 0:
    # Factorial is not defined for negative numbers
    print("Factorial does not exist")  
elif num == 0:
    # Special case: factorial of 0 is 1
    print("The factorial of 0 is 1")  
else:
    # Calculate and print the factorial for positive numbers
    print("The factorial of", num, "is", factorial(num))

```

## 2.Roman to integer Converter
This code defines a function i_r(n) that converts a given integer n into its Roman numeral representation. It uses a mapping of Roman numerals to their integer values, iteratively appending the appropriate symbols to the result string based on the input number. The program prompts the user for an integer input and then outputs the corresponding Roman numeral.

```python
class integer():
    # Method to convert an integer to its Roman numeral representation
    def integer_to_roman(self, nums):
        # List of tuples mapping integer values to their corresponding Roman numeral symbols
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        # Initialize an empty string to build the Roman numeral
        roman = ""

        # Iterate over each tuple in the values list
        for i in values:
            # While the current number (nums) is greater than or equal to the integer value
            while nums >= i[0]:
                # Append the corresponding Roman numeral symbol to the result string
                roman += i[1]
                # Decrease the number by the integer value
                nums -= i[0]

        # Return the final Roman numeral string
        return roman            

# Prompt the user to enter a number
s = int(input("Enter a number: "))

# Create an instance of the integer class
op = integer()

# Call the method to convert the integer to Roman numeral and print the result
print(op.integer_to_roman(s))

```

## 3.Word Reversal 
This code defines a Word class that can reverse the order of words in a given string. It initializes with a word and contains a method reverse() that splits the string into individual words, reverses their order, and then joins them back into a single string. An instance of the class is created with the string "hello world" ,and the reversed result is printed.

```python
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

```
## 4.Remove Duplicates with Maximum Two Occurrences

This code defines a function r_d(l) that removes excess duplicates from a sorted list, ensuring that each element appears at most twice. The list is first sorted, and then the function iterates through the list to check if any element occurs more than twice. If it does, it removes the extra occurrences and appends a placeholder (underscore) to maintain the list's length. The modified list is then returned and printed.

```python
def r_d(l):
    # Sort the list in ascending order
    l.sort()  
    # Iterate through the list, stopping before the last two elements
    for i in range(len(l) - 2):
        # Check if the current element is equal to the element two positions ahead  
        while l[i] == l[i + 2]:  
            # Remove the duplicate element
            l.remove(l[i])  
            # Append a placeholder to maintain list length
            l.append("_")  
            
    return l  # Return the modified list

# Input list with duplicates
list1 = [0, 1, 1, 1, 2, 2, 3, 3, 3]
# Call the function to remove excess duplicates
op = r_d(list1)
# Print the modified list with duplicates removed
print(f"Removed sorted duplicate list {op}")
```
## 5.Rotate the array

This code defines a function that rotates a given list to the right by  positions. The function uses a loop to remove the last element of the list and insert it at the beginning. This process is repeated times. Finally, the modified list is returned and printed.

```python

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

```