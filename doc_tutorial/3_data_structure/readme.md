
---

# Python Data Structures Summary

The Python data structures tutorial page provides an overview of built-in data types and their operations. This section covers lists, tuples, sets, and dictionaries, as well as some common operations and methods associated with these data types.

## Data Structures

### 1. Lists

Lists are ordered collections of items that can be of different types. They are mutable, meaning that you can change their content.

**Syntax:**
```python
my_list = [item1, item2, item3]
```

- **Common Methods:**
  - `append(item)`: Adds an item to the end of the list.
  - `extend(iterable)`: Extends the list by appending elements from an iterable.
  - `remove(item)`: Removes the first occurrence of an item.
  - `pop([index])`: Removes and returns an item at the given position in the list.

### 2. Tuples

Tuples are ordered collections of items, similar to lists, but they are immutable, meaning their content cannot be changed once created.

**Syntax:**
```python
my_tuple = (item1, item2, item3)
```

- **Common Operations:**
  - Accessing elements by index: `my_tuple[index]`
  - Slicing: `my_tuple[start:stop]`
  - Concatenation: `tuple1 + tuple2`

### 3. Sets

Sets are unordered collections of unique items. They support mathematical operations like union, intersection, and difference.

**Syntax:**
```python
my_set = {item1, item2, item3}
```

- **Common Methods:**
  - `add(item)`: Adds an item to the set.
  - `remove(item)`: Removes an item from the set.
  - `union(other_set)`: Returns the union of the set and another set.
  - `intersection(other_set)`: Returns the intersection of the set and another set.

### 4. Dictionaries

Dictionaries are unordered collections of key-value pairs. They are mutable and allow for fast lookups by key.

**Syntax:**
```python
my_dict = {key1: value1, key2: value2}
```

- **Common Methods:**
  - `get(key, default)`: Returns the value for the specified key, or `default` if the key is not found.
  - `keys()`: Returns a view object of all the keys in the dictionary.
  - `values()`: Returns a view object of all the values in the dictionary.
  - `items()`: Returns a view object of all the key-value pairs in the dictionary.

## Practice Questions

### Easy

1. **List Operations:**
   Create a list of five integers and perform the following operations:
   - Append the number 6 to the list.
   - Remove the number 3 from the list.
   - Print the length of the list.

   **Sample Output:**
   ```
   [1, 2, 4, 5, 6]
   Length: 5
   ```

2. **Tuple Indexing:**
   Create a tuple with three strings and access the second element.

   **Expected Output:**
   ```
   second_element
   ```

3. **Set Membership:**
   Create a set with three elements and check if a specific element is in the set.

   **Sample Output:**
   - For a set `{1, 2, 3}` and element `2`: `True`
   - For a set `{1, 2, 3}` and element `4`: `False`

### Medium

4. **Set Operations:**
   Create two sets and perform the following operations:
   - Find the union of the sets.
   - Find the intersection of the sets.

   **Sample Sets:**
   - Set A: `{1, 2, 3}`
   - Set B: `{3, 4, 5}`

   **Expected Output:**
   ```
   Union: {1, 2, 3, 4, 5}
   Intersection: {3}
   ```

5. **Dictionary Key-Value Pairs:**
   Create a dictionary with five key-value pairs and print all keys and values separately.

   **Sample Output:**
   ```
   Keys: ['key1', 'key2', 'key3', 'key4', 'key5']
   Values: ['value1', 'value2', 'value3', 'value4', 'value5']
   ```

6. **List Slicing:**
   Given a list, slice it to get the first three elements.

   **Sample List:** `[10, 20, 30, 40, 50]`

   **Expected Output:**
   ```
   [10, 20, 30]
   ```

### Hard

7. **Nested Dictionaries:**
   Create a nested dictionary with students' names as keys and their scores in three subjects as values. Calculate the average score for a given student.

   **Sample Dictionary:**
   ```python
   students = {
       'Alice': {'math': 85, 'science': 90, 'english': 88},
       'Bob': {'math': 78, 'science': 85, 'english': 80}
   }
   ```

   **Expected Output:**
   - For `Alice`: `Average score: 87.67`
   - For `Bob`: `Average score: 81.00`

8. **Tuple Unpacking:**
   Given a list of tuples, unpack each tuple into separate variables and print them.

   **Sample List of Tuples:**
   ```python
   tuples_list = [(1, 'a'), (2, 'b'), (3, 'c')]
   ```

   **Sample Output:**
   ```
   1 a
   2 b
   3 c
   ```

9. **Dictionary Comprehension:**
   Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 and the values are their squares.

   **Expected Output:**
   ```python
   {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
   ```

---

Feel free to use this Markdown content for your README file or modify it as needed. Let me know if you need any further assistance!