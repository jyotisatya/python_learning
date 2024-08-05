
---

# Python Tutorial: Conditional Statements

## Introduction

Conditional statements in Python allow you to control the flow of your program by making decisions based on conditions. This tutorial will cover the basics of `if`, `elif`, `else` statements, inline conditional operations, type checking, and working with simple and nested structures. By the end, you'll have a solid understanding of how to implement conditional logic in Python.

## 1. Basic Conditional Statements

### `if` Statement

The `if` statement evaluates a condition and executes the block of code if the condition is `True`.

**Syntax:**

```python
if condition:
    # Code to execute if condition is True
```

**Example:**

```python
# Check if a number is positive
number = 5

if number > 0:
    print("The number is positive.")
```

**Explanation:**

- **Condition**: The condition `number > 0` is evaluated. If it returns `True`, the indented code block is executed.
- **Output**: Since `5` is greater than `0`, the output is `"The number is positive."`

### `else` Statement

The `else` statement executes a block of code if the preceding `if` statement is `False`.

**Syntax:**

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

**Example:**

```python
# Check if a number is positive or non-positive
number = -3

if number > 0:
    print("The number is positive.")
else:
    print("The number is non-positive.")
```

**Explanation:**

- **`else` Block**: Executes when `number > 0` is `False`.
- **Output**: `"The number is non-positive."` because `-3` is not greater than `0`.

### `elif` Statement

The `elif` (short for "else if") statement allows you to check multiple conditions.

**Syntax:**

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition1 is False and condition2 is True
else:
    # Code to execute if all conditions are False
```

**Example:**

```python
# Determine if a number is positive, negative, or zero
number = 0

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Explanation:**

- **Multiple Conditions**: Checks conditions in order. If all are `False`, executes `else`.
- **Output**: `"The number is zero."` since `number` is `0`.

## 2. Inline Conditional Operations

Inline conditional operations (also known as the ternary operator) provide a concise way to perform simple conditional logic.

**Syntax:**

```python
value_if_true if condition else value_if_false
```

**Example:**

```python
# Determine if a number is even or odd using inline conditional operation
number = 4

result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}.")
```

**Explanation:**

- **Inline Conditional**: `(value_if_true if condition else value_if_false)` is evaluated. 
- **Output**: `"The number is even."` because `4 % 2 == 0` is `True`.

### Nested Inline Conditional

You can nest inline conditionals for more complex logic.

**Example:**

```python
# Determine the grade based on score using nested inline conditional
score = 85

grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(f"The grade is {grade}.")
```

**Explanation:**

- **Nested Inline**: Nested conditionals to assign grades.
- **Output**: `"The grade is B."` because `85 >= 80` is `True`.

## 3. Logical Operators

Logical operators (`and`, `or`, `not`) allow you to combine multiple conditions.

### `and` Operator

The `and` operator returns `True` if both conditions are `True`.

**Example:**

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter the concert.")
```

**Explanation:**

- **Both Conditions**: Both `age >= 18` and `has_ticket` must be `True`.
- **Output**: `"You can enter the concert."`

### `or` Operator

The `or` operator returns `True` if at least one condition is `True`.

**Example:**

```python
is_raining = False
has_umbrella = True

if is_raining or has_umbrella:
    print("You can go outside.")
```

**Explanation:**

- **At Least One Condition**: Either `is_raining` or `has_umbrella` must be `True`.
- **Output**: `"You can go outside."`

### `not` Operator

The `not` operator inverts the truth value of a condition.

**Example:**

```python
is_sunny = False

if not is_sunny:
    print("It is not sunny outside.")
```

**Explanation:**

- **Inverted Condition**: The condition `not is_sunny` is `True` because `is_sunny` is `False`.
- **Output**: `"It is not sunny outside."`

## 4. Checking Types and Instances

In Python, you can check the type and instance of a variable using the `type()` and `isinstance()` functions.

### `type()` Function

The `type()` function returns the type of an object.

**Example:**

```python
# Check the type of a variable
value = 42

if type(value) == int:
    print("The variable is an integer.")
```

**Explanation:**

- **Type Check**: `type(value)` returns the type of `value`.
- **Output**: `"The variable is an integer."`

### `isinstance()` Function

The `isinstance()` function checks if an object is an instance of a class or a tuple of classes.

**Example:**

```python
# Check if a variable is an instance of a specific type
value = [1, 2, 3]

if isinstance(value, list):
    print("The variable is a list.")
```

**Explanation:**

- **Instance Check**: `isinstance(value, list)` returns `True` if `value` is a list.
- **Output**: `"The variable is a list."`

## 5. Working with Simple and Nested Structures

Python supports simple and nested data structures such as lists and dictionaries. Conditional statements can be used to navigate and manipulate these structures.

### Simple Structures

**Example: List**

```python
# Check if an element exists in a list
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Banana is in the list.")
```

**Explanation:**

- **Membership Check**: `"banana" in fruits` returns `True` if `"banana"` is in the list.
- **Output**: `"Banana is in the list."`

**Example: Dictionary**

```python
# Access dictionary values using conditions
person = {"name": "Alice", "age": 25}

if "age" in person:
    print(f"Age: {person['age']}")
```

**Explanation:**

- **Key Existence**: `"age" in person` checks if the key `"age"` exists in the dictionary.
- **Output**: `"Age: 25"`

### Nested Structures

**Example: Nested List**

```python
# Access nested list elements
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

if matrix[1][1] == 5:
    print("The element is 5.")
```

**Explanation:**

- **Nested Access**: `matrix[1][1]` accesses the element at the second row and second column.
- **Output**: `"The element is 5."`

**Example: Nested Dictionary**

```python
# Access nested dictionary values
student = {
    "name": "Bob",
    "grades": {
        "math": 90,
        "science": 85
    }
}

if student["grades"]["math"] > 80:
    print("Math grade is above 80.")
```

**Explanation:**

- **Nested Access**: `student["grades"]["math"]` accesses the math grade in the nested dictionary.
- **Output**: `"Math grade is above 80."`

## Practice Assignments

### Easy

1. **Positive or Negative:**
   Write a program that takes an integer input from the user and determines if it is positive or negative.

   **Sample Input:**
   ```
   -5
   ```

   **Expected Output:**
   ```
   The number is negative.
   ```

2. **Even or Odd:**
   Write a program that takes an integer input from the user and determines if it is even or odd using inline conditional operations.

   **Sample Input:**
   ```
   8
   ```

   **Expected Output:**
   ```


   The number is even.
   ```

### Medium

3. **Grade Calculator:**
   Write a program that calculates a student's grade based on their score using nested inline conditionals. The grading criteria are:
   - 90 and above: A
   - 80 to 89: B
   - 70 to 79: C
   - Below 70: D

   **Sample Input:**
   ```
   88
   ```

   **Expected Output:**
   ```
   The grade is B.
   ```

4. **List Element Check:**
   Write a program to check if a given element exists in a list and print a message accordingly.

   **Sample Input:**
   ```
   List: [2, 4, 6, 8]
   Element: 4
   ```

   **Expected Output:**
   ```
   The element 4 exists in the list.
   ```

### Hard

5. **Complex Condition Evaluation:**
   Write a program that evaluates complex conditions using logical operators. Determine if a user is eligible for a discount based on their membership status and purchase amount.

   **Conditions:**
   - Gold members get a discount for any purchase amount.
   - Silver members get a discount if the purchase amount is above $100.
   - Non-members do not get a discount.

   **Sample Input:**
   ```
   Membership: Silver
   Purchase Amount: $120
   ```

   **Expected Output:**
   ```
   You are eligible for a discount.
   ```

6. **Nested Dictionary Navigation:**
   Write a program to navigate a nested dictionary and print a specific value based on user input. Use `isinstance()` to ensure the value exists and is of the correct type.

   **Sample Dictionary:**
   ```python
   data = {
       "users": {
           "alice": {
               "age": 30,
               "email": "alice@example.com"
           },
           "bob": {
               "age": 25,
               "email": "bob@example.com"
           }
       }
   }
   ```

   **Sample Input:**
   ```
   User: alice
   Attribute: email
   ```

   **Expected Output:**
   ```
   Email: alice@example.com
   ```

---

Feel free to ask if you have any questions or need further clarification!