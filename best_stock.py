def max_profit(prices):
    # If the prices list is empty, return 0 profit
    if not prices:
        return 0
     # Initialize the minimum price to infinity
    minp = float("inf") 
     # Initialize the maximum profit to 0
    maxp = 0 
    
    # Iterate through each price in the list
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < minp: 
            minp = price
        
        # Calculate the current profit by subtracting the minimum price from the current price
        current = price - minp
        
        # Update the maximum profit if the current profit is greater
        if current > maxp:
            maxp = current
     # Return the maximum profit found
    return maxp 

# Example prices
prices = [7, 1, 5, 3, 6, 4]
# Calculate the maximum profit
p = max_profit(prices)
# Print the result
print(p)  
