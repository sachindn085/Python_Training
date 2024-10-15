def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Loop n times to generate Fibonacci numbers
    for _ in range(n):
        # Yield the current Fibonacci number
        yield a  
        # Update a and b to the next two Fibonacci numbers
        a, b = b, a + b

# Set the number of Fibonacci terms to generate
n = 10  
# Print the list of the first n Fibonacci numbers by converting the generator to a list
print(list(fibonacci(n)))
