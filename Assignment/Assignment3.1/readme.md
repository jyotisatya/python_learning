# Nested dictionary data access


```python
# Sample 4-5 level nested dictionary
nested_dict = {
    "level1": {
        "level2": {
            "level3": {
                "int_value": 42,
                "float_value": 3.14,
                "str_value": "Hello",
                "list_value": [1, 2, 3, 4, 5],
                "bool_value": True
            },
            "another_level3": {
                "nested_list": [
                    {"name": "Alice", "age": 25},
                    {"name": "Bob", "age": 30}
                ],
                "nested_dict": {
                    "key1": "value1",
                    "key2": "value2"
                }
            }
        },
        "simple_list": ["apple", "banana", "cherry"],
        "simple_dict": {
            "keyA": "valueA",
            "keyB": "valueB"
        }
    },
    "simple_int": 10,
    "simple_float": 20.5,
    "simple_str": "Nested Dictionary Example"
}

# Print the nested dictionary
print(nested_dict)
```

### Assignment Tasks for Beginners

1. **Accessing Values:**
   - Print the value of `"int_value"` from `nested_dict`.
   - Print the second element of the `list_value`.

2. **Modifying Values:**
   - Change the `"str_value"` to `"Hello, World!"`.
   - Add a new element to the `list_value`.

3. **Adding New Keys:**
   - Add a new key-value pair to `nested_dict["level1"]["simple_dict"]`.

4. **Removing Keys:**
   - Remove the key `"simple_int"` from `nested_dict`.

5. **Looping through the Dictionary:**
   - Write a loop to print all keys and values in `nested_dict["level1"]["simple_dict"]`.

### Sample Solutions

```python
