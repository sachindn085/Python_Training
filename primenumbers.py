def prime_numbers(n1, n2):
        # Initialize an empty set to store prime numbers
        prime = set()
        
        # Iterate through the range from n1 to n2 (inclusive)
        for i in range(n1, n2 + 1):
            # Check if the number is greater than 1 (only positive integers greater than 1 can be prime)
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