```python
def factorial(number):
  if number < 0:
    print('error')
    return 
  factorial = 1
  while number >= 1:
    
    factorial = factorial * number
    number = number-1
  return factorial  
    
    

result = factorial(-1)
print (result)
```

To handle negative values in the factorial function properly, you can modify the function to return an appropriate error message or raise an exception instead of just printing "error" and returning None. This ensures that the function behaves predictably when given a negative input. Here's how you can handle it:


```python
def factorial(number):
    if number < 0:
        return "Error: Factorial is not defined for negative numbers."
    
    factorial = 1
    while number >= 1:
        factorial *= number
        number -= 1
        
    return factorial

result = factorial(-1)
print(result)

```

This may not be correct approach

Returning a string for error cases and an integer for success cases can make the function's output inconsistent. A more consistent approach is to handle errors by either returning a specific value (e.g., `None` or `-1`) for error cases or by raising an exception. 

Here are a couple of approaches that maintain consistency:

### Option 1: Return `None` for Error Cases
You can return `None` when the input is negative, indicating that the factorial cannot be computed.

```python
def factorial(number):
    if number < 0:
        return None  # Indicating an error case
    
    factorial = 1
    while number >= 1:
        factorial *= number
        number -= 1
        
    return factorial

result = factorial(-1)
if result is None:
    print("Error: Factorial is not defined for negative numbers.")
else:
    print(result)
```

- **Explanation:** This version returns `None` for negative numbers. The calling code checks if the result is `None` and handles the error appropriately.

### Option 2: Raise an Exception
Raising an exception is often preferred because it separates error handling from normal control flow.

```python
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    factorial = 1
    while number >= 1:
        factorial *= number
        number -= 1
        
    return factorial

try:
    result = factorial(-1)
    print(result)
except ValueError as e:
    print(e)
```

- **Explanation:** This version raises a `ValueError` for negative inputs. The exception is caught and handled in the `try-except` block, ensuring that the function consistently returns an integer for valid inputs.

### Summary
- **Option 1 (Return `None`):** Returns `None` for negative inputs, keeping the return type consistent, and allows the calling code to handle the error.
- **Option 2 (Raise Exception):** Raises an exception for negative inputs, making the error handling more explicit and separating it from the normal flow of the program.

Both approaches ensure that your function consistently returns an integer for valid inputs and handles errors appropriately.