
---
# Variable and Scope

Here's a breakdown of the code and the expected output for each `print` statement:

### Code Analysis

```python
scope = 5
print(scope)  # 1st print

def fact(n):
    result = 1
    scope = 7
    print(scope)  # 2nd print
    while n > 0:
        result = n
        n = n - 1
        scope = n
    print(scope)  # 3rd print
    return result

scope = 78
print(scope)  # 4th print
sol = fact(4)
```

### Output and Explanation

1. **First `print(scope)` (outside the function):**
   - **Output:** `5`
   - **Reason:** The variable `scope` is first assigned the value `5`. The first `print(scope)` will output this value.

2. **Second `print(scope)` (inside the `fact` function):**
   - **Output:** `7`
   - **Reason:** Inside the `fact` function, a new local variable `scope` is assigned the value `7`. The `print(scope)` inside the function will output this local variable value, which is `7`. This local variable `scope` does not affect the global `scope` defined outside the function.

3. **Third `print(scope)` (inside the `fact` function, after the `while` loop):**
   - **Output:** `0`
   - **Reason:** The `while` loop continues as long as `n > 0`. Inside the loop, `n` is decremented by `1` each time, and `scope` is updated to `n`. After the loop ends (when `n` becomes `0`), the `print(scope)` will output `0`, which is the value of `n` when the loop terminates.

4. **Fourth `print(scope)` (outside the function after reassigning):**
   - **Output:** `78`
   - **Reason:** After the `fact` function is defined, the global `scope` variable is reassigned to `78`. The last `print(scope)` will output the value of this global variable, which is now `78`.

### Summary of Output:

1. `5`
2. `7`
3. `0`
4. `78`

### Detailed Explanation:

- The first `print` statement outputs `5` because it refers to the global `scope` variable initially set to `5`.
- Inside the `fact` function, a local variable named `scope` is defined and assigned `7`. This is why the second `print` outputs `7`.
- As the loop in the `fact` function modifies `n`, it also updates the local `scope` variable to the current value of `n`. When `n` reaches `0`, the loop ends, and the third `print` outputs `0`.
- Finally, after calling the `fact` function, the global `scope` variable is set to `78`, and the fourth `print` reflects this new value, outputting `78`.

This demonstrates the difference between global and local variable scopes in Python.

# Python Control Flow Summary

The Python control flow tutorial page provides an overview of various control flow statements used in Python, which allow for conditional execution of code and looping over data. This section covers `if` statements, `for` loops, `while` loops, `break`, `continue`, and the `pass` statement, as well as the `match` statement introduced in Python 3.10.

## Control Flow Tools

### 1. `if` Statements

`if` statements allow conditional execution of code blocks. They can include optional `elif` (else-if) and `else` clauses to handle multiple conditions.

**Syntax:**
```python
if condition:
    # Code block
elif another_condition:
    # Another code block
else:
    # Else block
```

### 2. `for` Loops

`for` loops iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each element.

**Syntax:**
```python
for variable in sequence:
    # Code block
```

- The `range()` function is often used with `for` loops to generate a sequence of numbers.

### 3. `while` Loops

`while` loops execute a block of code as long as a specified condition is true.

**Syntax:**
```python
while condition:
    # Code block
```

### 4. `break` and `continue` Statements

- `break` is used to exit a loop prematurely.
- `continue` is used to skip the current iteration and continue with the next one.

### 5. `pass` Statement

The `pass` statement is a no-operation statement used as a placeholder where syntactically some code is required but you do not want any code to execute.

**Syntax:**
```python
pass
```

### 6. `match` Statement (Python 3.10+)

The `match` statement provides a structural pattern matching mechanism that allows for more sophisticated conditional logic.

**Syntax:**
```python
match variable:
    case pattern1:
        # Code block
    case pattern2:
        # Code block
    case _:
        # Default block
```

## Practice Questions

### Easy

1. **Fibonacci Sequence:**
   Write a `for` loop that prints the first 10 numbers in the Fibonacci sequence.
   
   **Expected Output:**
   ```
   0
   1
   1
   2
   3
   5
   8
   13
   21
   34
   ```

2. **Even Numbers:**
   Use a `while` loop to print all even numbers between 1 and 20.

   **Expected Output:**
   ```
   2
   4
   6
   8
   10
   12
   14
   16
   18
   20
   ```

3. **Simple if-else:**
   Write an `if-else` statement that prints "Even" if a number is even and "Odd" if a number is odd.

   **Sample Output:**
   - For input `4`: `Even`
   - For input `7`: `Odd`

### Medium

4. **Prime Numbers:**
   Write a program using a `for` loop that checks if a number is prime.

   **Sample Output:**
   - For input `5`: `Prime`
   - For input `10`: `Not Prime`

5. **List Summation:**
   Use a `for` loop to calculate the sum of all numbers in a list.

   **Sample List:** `[1, 2, 3, 4, 5]`

   **Expected Output:**
   ```
   15
   ```

6. **Password Verification:**
   Write a `while` loop that repeatedly asks for a password until the correct password ("python123") is entered.

   **Sample Interaction:**
   ```
   Enter password: test
   Enter password: python123
   Password accepted!
   ```

### Hard

7. **Number Guessing Game:**
   Create a number guessing game where the user has to guess a number between 1 and 100. Provide feedback if the guess is too high or too low. Use `while` loop and `break` statement to exit when the correct number is guessed.

   **Sample Interaction:**
   ```
   Guess a number between 1 and 100: 50
   Too low!
   Guess a number between 1 and 100: 75
   Too high!
   Guess a number between 1 and 100: 60
   Correct!
   ```

8. **Pattern Matching:**
   Using the `match` statement, create a program that matches different shapes (e.g., "circle", "square", "triangle") and prints the number of sides they have. Default case should handle unknown shapes.

   **Sample Output:**
   - For input `"circle"`: `This shape has no sides.`
   - For input `"square"`: `This shape has 4 sides.`
   - For input `"triangle"`: `This shape has 3 sides.`
   - For input `"pentagon"`: `Unknown shape.`

9. **Factorial Calculation:**
   Write a recursive function to calculate the factorial of a number. Use control flow statements to handle base cases.

   **Sample Output:**
   - For input `5`: `120`
   - For input `0`: `1`

---

Feel free to adjust the questions or expected answers based on your learning needs! Let me know if you need more content or additional pages.