#Solutions assignment 3.1
Section 1:


### Solutions

1. Print the value of `"float_value"` from `nested_dict`.
   ```python
   print(nested_dict["level1"]["level2"]["level3"]["float_value"])  # Output: 3.14
   ```

2. Print the value of `"str_value"` from `nested_dict`.
   ```python
   print(nested_dict["level1"]["level2"]["level3"]["str_value"])  # Output: Hello
   ```

3. Print the value of the third element in the `list_value`.
   ```python
   print(nested_dict["level1"]["level2"]["level3"]["list_value"][2])  # Output: 3
   ```

4. Print the value of `"bool_value"` from `nested_dict`.
   ```python
   print(nested_dict["level1"]["level2"]["level3"]["bool_value"])  # Output: True
   ```

5. Print the value of `"name"` for the first dictionary inside the `"nested_list"`.
   ```python
   print(nested_dict["level1"]["level2"]["another_level3"]["nested_list"][0]["name"])  # Output: Alice
   ```

6. Print the value of `"age"` for the second dictionary inside the `"nested_list"`.
   ```python
   print(nested_dict["level1"]["level2"]["another_level3"]["nested_list"][1]["age"])  # Output: 30
   ```

7. Print the value of `"key1"` from the nested dictionary inside `"another_level3"`.
   ```python
   print(nested_dict["level1"]["level2"]["another_level3"]["nested_dict"]["key1"])  # Output: value1
   ```

8. Print the value of the first element in the `"simple_list"`.
   ```python
   print(nested_dict["level1"]["simple_list"][0])  # Output: apple
   ```

9. Print the value of `"keyA"` from `"simple_dict"`.
   ```python
   print(nested_dict["level1"]["simple_dict"]["keyA"])  # Output: valueA
   ```

10. Print the value of `"simple_float"` from `nested_dict`.
    ```python
    print(nested_dict["simple_float"])  # Output: 20.5
    ```

11. Print the value of `"simple_str"` from `nested_dict`.
    ```python
    print(nested_dict["simple_str"])  # Output: Nested Dictionary Example
    ```

Section 2

```python

# Accessing Values
print(nested_dict["level1"]["level2"]["level3"]["int_value"])
print(nested_dict["level1"]["level2"]["level3"]["list_value"][1])

# Modifying Values
nested_dict["level1"]["level2"]["level3"]["str_value"] = "Hello, World!"
nested_dict["level1"]["level2"]["level3"]["list_value"].append(6)

# Adding New Keys
nested_dict["level1"]["simple_dict"]["keyC"] = "valueC"

# Removing Keys
del nested_dict["simple_int"]

# Looping through the Dictionary
for key, value in nested_dict["level1"]["simple_dict"].items():
    print(f"{key}: {value}")


```