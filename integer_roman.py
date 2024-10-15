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
