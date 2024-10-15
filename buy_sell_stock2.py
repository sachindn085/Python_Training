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
