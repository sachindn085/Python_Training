# DAY 2: 10/10/2024
# Problem Solving in Python

## Problem 1: Sorting a List Without Using `sort()`

To sort a list without utilizing the built-in `sort()` method, we can implement the Bubble Sort algorithm. This algorithm repeatedly traverses the list, compares adjacent elements, and swaps them if they are in the incorrect order. This process is repeated until the entire list is sorted.

### Example Code:
```python
# Initialize a list of integers
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
```

### Explanation:
- The outer loop iterates over each element in the list.
- The inner loop compares adjacent elements and swaps them if needed.
- This continues until the list is fully sorted.

## Problem 2: Finding the Longest Common Prefix Using Sorting
To determine the longest common prefix among a list of strings, we can sort the list and then compare the first and last strings. The longest common prefix consists of the characters they share from the start.

### Example Code:
```python
s= ["door", "done", "dog"]
def comman_brackets(str):
    if not str:
        return ""
    
    # Sort the list of strings
    str.sort()
    
    # The longest common prefix will be between the first and the last string
    first = str[0]
    last = str[-1]
    i = 0
    
    # Compare characters until they differ
    while    first[i] == last[i]:
        i += 1
    
    return first[:i]
print(comman_brackets(s)) 
```

### Explaination:
- The code checks if the list is empty and prints a message if it is.
- The list is sorted to arrange the strings.
- It compares the first and last strings to find matching characters.
- The common prefix is constructed until a mismatch occurs, and the result is displayed.

## Problem 3: Roman Numeral Converter
To convert a string representing a Roman numeral into its integer equivalent, you can use the following code.

### Example Code:
```python
# Function to convert Roman numeral to integer
def roman_to_integer(roman):
    # Dictionary to map Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0  # Initialize total to 0
    
    # Iterate over each character in the Roman numeral
    for i in range(len(roman)):
        # Get the integer value of the current Roman numeral
        current_value = roman_values[roman[i]]  
        
        # If this is not the last character and the next character represents a larger value
        if i < len(roman) - 1 and current_value < roman_values[roman[i + 1]]:
            # Subtract the current value
            total -= current_value  
        else:
            # Otherwise, add the current value
            total += current_value 
            # Return the computed integer value 
    return total  
roman_numeral = "CII"
result = roman_to_integer(roman_numeral)
print(f"The integer value of '{roman_numeral}' is {result}.")

```
### Explanation:
- A dictionary, maps each Roman numeral to its corresponding integer value.
- The function iterates through the string, checking if the current numeral is less than the next. If it is, its value is subtracted; otherwise, it is added to the total.
css
