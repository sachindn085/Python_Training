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
