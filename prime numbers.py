def is_prime(num):
    if num <= 1:
        # Numbers less than or equal to 1 are not prime
        return False  
    # Check for factors up to the square root of num
    for i in range(2, (num//2) + 1):  
        if num % i == 0:
            # If num is divisible by i, it is not prime
            return False  
        # If no divisors are found, it is prime
    return True  

def generate_primes(limit):
    
    # Initialize an empty list to store prime numbers
    primes = []  
    # Loop through numbers from 2 to limit
    for num in range(2, limit + 1):  
        if is_prime(num):
            # If num is prime, add it to the list
            primes.append(num)  
             # Return the list of prime numbers
    return primes 

# Set the upper limit for prime generation
limit = 20  
primes_list = generate_primes(limit)  
print(primes_list)  
