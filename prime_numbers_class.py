class prime_numbers:
    def __init__(self):
        # Initialize an empty list to store prime numbers
        self.primes = []

    def prime(self, num):
        # Check if a number is prime
        if num <= 1:
            # Numbers less than or equal to 1 are not prime
            return False  
        # Check for factors from 2 to num // 2
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                # If num is divisible by i, it is not prime
                return False  
            # If no divisors are found, num is prime
        return True  

    def generate_prime(self, limit):
        # Generate all prime numbers up to the specified limit
        for num in range(2, limit + 1):
            # Check if num is prime
            if self.prime(num):  
                # Add prime number to the list
                self.primes.append(num)  
        return self.primes  # Return the list of generated prime numbers

# Create an instance of the prime_numbers class
op = prime_numbers()

# Set the limit for prime number generation
limit = 10

# Print the list of prime numbers up to the specified limit
print(op.generate_prime(limit))

