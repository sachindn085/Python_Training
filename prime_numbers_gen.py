def is_prime(n):
    if n <= 1:
        # Numbers less than or equal to 1 are not prime
        return False  
    for i in range(2, ((n // 2) + 1)):
        # Check for factors from 2 to n/2
        if n % i == 0:
            # If n is divisible by any i, it's not prime
            return False  
        # If no factors were found, n is prime
    return True  

def prime_nums_generator():
    # Start checking for prime numbers from 2
    n = 2  
    # Infinite loop to generate primes
    while True:  
        if is_prime(n):
             # Yield the prime number found
            yield n 
            # Move to the next number
        n += 1  
# Create a generator object for prime numbers
primes = prime_nums_generator()

# Get user input for how many prime numbers to generate
n = int(input("Input the number of prime numbers you want to generate: "))

print("First", n, "Prime numbers:")
# Generate and print the first n prime numbers
for _ in range(n):
    # Get the next prime number from the generator
    print(next(primes))  
