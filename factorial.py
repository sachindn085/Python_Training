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
