# An Informal Introduction to Python

# Python 3.12 Tutorial Introduction

## Summary

### Overview of Python
- Python is an interpreted, high-level programming language known for its readability and ease of use. 
- Supports multiple programming paradigms: procedural, object-oriented, and functional programming.

### Python as a Calculator
- Interactive mode allows using Python like a calculator for basic arithmetic operations.
- **Operators**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponentiation).
- **Examples**:
  - `2 + 2` results in `4`
  - `50 - 5*6` results in `20`
  - `8 / 5` results in `1.6` (division always returns a float)
  - `17 // 3` results in `5` (floor division)
  - `17 % 3` results in `2` (remainder)
  - `5 ** 2` results in `25` (5 squared)

### Data Types
- **Integers**: Whole numbers, unlimited in size.
- **Floating Point Numbers**: Numbers with decimal points, such as `3.14` or `-0.5`.
- **Strings**: Text data enclosed in quotes. You can use single (`'`), double (`"`), or triple quotes (`'''` or `"""` for multi-line strings).
- **Examples**:
  - `'Hello'`, `"World"`, `'''Hello World'''`

### String Operations
- Strings can be concatenated using `+` and repeated with `*`.
- **Indexing**: Access characters using zero-based indices, like `word[0]` for the first character.
- **Slicing**: Extract substrings using `[start:end]`, where `start` is inclusive, and `end` is exclusive.
- **Examples**:
  - `'Py' + 'thon'` results in `'Python'`
  - `'A' * 3` results in `'AAA'`
  - `'Python'[0]` results in `'P'`
  - `'Python'[1:4]` results in `'yth'`

### Lists
- A list is a collection of items, which can be of different types, enclosed in square brackets.
- Lists are mutable, allowing you to change their content.
- **Operations**:
  - Concatenate using `+`.
  - Slice similar to strings.
  - Use `append()` to add elements.
  - Access elements with indices.
- **Examples**:
  - `[1, 2, 3] + [4, 5, 6]` results in `[1, 2, 3, 4, 5, 6]`
  - `list = [1, 2, 3]`
  - `list.append(4)` results in `[1, 2, 3, 4]`
  - `list[0]` results in `1`

## Practice Questions

### Very Easy

1. **Basic Arithmetic**:
   - Calculate the result of \( 15 + 5 \times 2 - 8 \div 4 \).

2. **String Concatenation**:
   - Create a string `"Hello"` and another string `"World"`, and concatenate them with a space in between.

3. **Access List Element**:
   - Given a list `fruits = ['apple', 'banana', 'cherry']`, print the first fruit in the list.

### Easy

4. **String Slicing**:
   - Given the string `s = "PythonProgramming"`, extract the substring `"Pro"` using slicing.

5. **List Manipulation**:
   - Create a list of numbers from 1 to 5. Add the number 6 to the list and then remove the number 2.

6. **String Repetition**:
   - Create a string `"Python"` and repeat it 3 times.

### Medium

7. **List Slicing**:
   - Given a list `numbers = [10, 20, 30, 40, 50, 60, 70]`, extract the sublist `[30, 40, 50]` using slicing.

8. **String Formatting**:
   - Format the string to display `"John is 25 years old"` using the variables `name = "John"` and `age = 25`.

9. **Nested Lists**:
   - Create a nested list `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` and print the element `5`.

### Hard

10. **Custom String Reversal**:
    - Write a function that takes a string as input and returns the string with each word reversed, but the word order is preserved.
    - Example: `"Hello World"` should return `"olleH dlroW"`.