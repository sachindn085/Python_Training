# Python Data Types and Their Methods



## 1. Numeric Types

### a. `int` 

### b. `float`

### c. `complex`



### 2. `list`
It reprsents the collection of elements
- **Methods**:
  - `append(x)`: Adds an item `x` to the end of the list.
  
    **Example**:
    ```python
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  
    ```

  - `remove(x)`: Removes the first occurrence of item `x` from the list. Raises a `ValueError` if `x` is not in the list.
  
    **Example**:
    ```python
    my_list.remove(2)
    print(my_list)  
    ```

  - `insert(i, x)`: Inserts item `x` at a given position `i`. The first argument is the index, and the second argument is the item to insert.
  
    **Example**:
    ```python
    my_list.insert(1, 2)
    print(my_list)  
    ```

  - `pop([i])`: Removes and returns the item at the given position `i` in the list. If no index is specified, `pop()` removes and returns the last item.
  
    **Example**:
    ```python
    popped_item = my_list.pop()
    print(popped_item)  
    ```

  - `sort()`: Sorts the items of the list in place (the arguments can be used for sort order).
  
    **Example**:
    ```python
    my_list.sort()
    print(my_list)  
    ```

### 3. `tuple`
It represents the collection elements and it is immutable
- **Methods**:
  - `count(x)`: Returns the number of times `x` appears in the tuple.
  
    **Example**:
    ```python
    my_tuple = (1, 2, 2, 3)
    print(my_tuple.count(2))  
    ```

  - `index(x[, start[, end]])`: Returns the index of the first occurrence of `x` in the tuple. Raises a `ValueError` if `x` is not found.
  
    **Example**:
    ```python
    print(my_tuple.index(3))  
    ```



### 4. `str`
It represents the sequence of characters which are enclosed in paranthesis
- **Methods**:
  - `upper()`: Converts all characters of the string to uppercase.
  
    **Example**:
    ```python
    my_string = "hello"
    print(my_string.upper())  
    ```

  - `split(sep=None)`: Splits the string into a list of substrings based on the specified separator.
  
    **Example**:
    ```python
    print(my_string.split('e'))  
    ```

  - `replace(old, new)`: Returns a copy of the string where all occurrences of substring `old` are replaced with `new`.
  
    **Example**:
    ```python
    print(my_string.replace("l", "r"))  
    ```

  - `find(sub)`: Returns the lowest index of the substring `sub` if found in the string; otherwise, it returns `-1`.
  
    **Example**:
    ```python
    print(my_string.find("e"))  
    ```

  - `join(iterable)`: Concatenates the elements of `iterable` into a single string, with the string as a separator.
  
    **Example**:
    ```python
    print(" ".join(["Hello", "World"]))  
    ```



### 5. `dict`
It represents the collection of key and value pairs
- **Methods**:
  - `keys()`: Returns a view object that displays a list of all the keys in the dictionary.
  
    **Example**:
    ```python
    my_dict = {'a': 1, 'b': 2}
    print(my_dict.keys())  
    ```

  - `values()`: Returns a view object that displays a list of all the values in the dictionary.
  
    **Example**:
    ```python
    print(my_dict.values())  
    ```

  - `items()`: Returns a view object that displays a list of dictionary's key-value tuple pairs.
  
    **Example**:
    ```python
    print(my_dict.items())  
    ```

  - `get(key[, default])`: Returns the value for `key` if `key` is in the dictionary; otherwise, it returns `default`.
  
    **Example**:
    ```python
    print(my_dict.get('a', 0))  
    print(my_dict.get('c', 0))  
    ```

  - `pop(key[, default])`: Removes the specified key and returns the corresponding value. If the key is not found, returns `default`.
  
    **Example**:
    ```python
    popped_value = my_dict.pop('a')  
    print(popped_value)  
    ```



### 6. `set`
It represents the collection of unique elements
- **Methods**:
  - `add(x)`: Adds an element `x` to the set.
  
    **Example**:
    ```python
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)  
    ```

  - `remove(x)`: Removes element `x` from the set. Raises a `KeyError` if `x` is not found.
  
    **Example**:
    ```python
    my_set.remove(2)
    print(my_set)  
    ```

  - `discard(x)`: Removes element `x` from the set if it is present. Does not raise an error if `x` is not found.
  
    **Example**:
    ```python
    my_set.discard(5)  
    ```

  - `union(other)`: Returns a new set with elements from the set and `other`.
  
    **Example**:
    ```python
    other_set = {3, 4, 5}
    print(my_set.union(other_set))  
    ```

  - `intersection(other)`: Returns a new set with elements common to the set and `other`.
  
    **Example**:
    ```python
    print(my_set.intersection(other_set))  
    ```


    ```

##  Type Casting

### a. `int()`

- **Example**:
  ```python
  num = "42"
  num_int = int(num)
  print(num_int)  
### b. `float()`
- **Example**:
```python
num = "3.14"
num_float = float(num)
print(num_float)  
```
### c. `str()`

- **Example**:
```python
num = 100
num_str = str(num)
print(num_str)  
```