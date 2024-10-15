# Day 4: 


## 1. Best Profit from Stock Prices

This program calculates the maximum profit that can be obtained by buying and selling stocks. It iterates through a list of stock prices and adds up the profits from any upward price movements. The function also prints the buying and selling prices that contribute to the profit.

```python
class stock:
    def max_profit(self, price):
        # Initialize profit to 0
        profit = 0
        
        # Loop through the price list starting from the second element
        for i in range(1, len(price)):
            # If the current price is greater than the previous price
            if price[i-1] < price[i]:
                # Calculate the profit by subtracting the previous price from the current price
                profit += price[i] - price[i-1]
        
        # Return the total profit
        return profit   

# Create an instance of the stock class
op = stock()

# Example list of stock prices
a = [2, 4, 3, 5, 6, 7, 2]

# Print the maximum profit that can be achieved
print(op.max_profit(a))

```

## 2. Prime Numbers in a Given Range

This program prompts the user to input two numbers and then finds all prime numbers between them. It uses a set to store unique prime numbers and checks each number in the range for primality by testing divisibility. The user can repeat the process as desired.

```python
while True:
    def prime_numbers(n1, n2):
        # Initialize an empty set to store prime numbers
        prime = set()
        
        # Iterate through the range from n1 to n2 (inclusive)
        for i in range(n1, n2 + 1):
            # Check if the number is greater than 1
            if i > 1:
                # Special case for the number 2, which is prime
                if i == 2:
                    prime.add(i)
                # Check for factors from 2 to i-1
                for j in range(2, i):
                    # If i is divisible by j, it is not a prime number
                    if (i % j) == 0:
                        break
                else:
                    # If no factors were found, i is a prime number
                    prime.add(i)
        
        # Print the set of prime numbers found in the range
        print("Prime numbers between", n1, "and", n2, "are:", prime)
    
    # Input: First number of the range
    n1 = int(input("Enter the first number : "))
    # Input: Second number of the range
    n2 = int(input("Enter the second number : "))
    # Call the function to find prime numbers in the specified range
    prime_numbers(n1, n2)
    print("\n")
    
    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    # If the user does not want to continue, break the loop
    if choice.lower() != 'y':
        break
```


## 3. Prime Numbers Generator

This version uses a generator to yield prime numbers in a specified range. Instead of returning a list, it yields one prime number at a time, allowing for memory-efficient processing. The program takes user input for the range and prints the first three prime numbers found.

```python
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


```

## 4. Prime using Class

This program defines a class Prime_fibb that computes both prime numbers up to a given input. It contains methods to check for primality, generate a list of primes. The user is prompted to enter a number, and the program displays prime numbers within that range.

```python
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



```

## 5. Fibonacci Series Generator

This program generates Fibonacci numbers up to a specified target using a generator function. It yields each Fibonacci number in the sequence until the target value is reached. The user inputs a target number, and the program prints all Fibonacci numbers less than that target.

```python
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


```