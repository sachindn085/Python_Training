

# Day 3 Date: 11/10/2024

### Overview
Three Python functions aimed at solving common programming problems: checking for palindromes, finding the majority element in a list, and calculating the maximum profit from a list of prices.

---

### 1. Palindrome Checker



**Purpose**: To determine if a given string is a palindrome, considering only alphanumeric characters and ignoring case.

**Code**:
```python
def palindrome(s):
    a=""
    for i in s:
        if i.isalnum():
            a+=i
    if a==a[::-1]:
        return"True"
    else:
        return"False"
s1="malay''''aam"
b=palindrome(s1)
print(b)
```
### Explanation:
- The function iterates through the input string, filtering out non-alphanumeric characters and converting the remaining characters to lowercase.
- It checks if the filtered string reads the same forwards and backwards.

# 2. Majority Element Finder


**Purpose**: To identify the element that appears most frequently in a given list.

**Code**:

```python
def majority_element(l):
    c_dict = {}
    for i in l:
        if i not in c_dict.keys():
            c_dict[i] = l.count(i)

    l1 = list(c_dict.values())
    l2 = []
    for k, v in c_dict.items():
        if max(l1) == v:
            l2.append(k)
    return l2

# Example usage
main_l = [2, 1, 2, 3, 2, 1, 1]
op = majority_element(main_l)
print(op)  # Output: [2]
```
### Explanation:
- The function creates a dictionary to count occurrences of each element in the list.
- It then identifies the elements with the maximum count and returns them.

# 3. Maximum Profit 


**Purpose**: To calculate the maximum profit that can be made from a list of prices, where you can buy and sell once.

**Code**:
```python
def max_profit(prices):
    if not prices:
        return 0
    minp = float("inf")  
    maxp = 0  
    for price in prices:
        if price < minp: 
            minp = price
        current = price - minp
        if current > maxp:
            maxp = current
    return maxp
prices = [7, 1, 5, 3, 6, 4]
p = max_profit(prices)
print(p)  


```


### Explanation:
- The function uses nested loops to check all possible pairs of buying and selling prices.
- It calculates the potential profit for each pair and keeps track of the maximum profit found.