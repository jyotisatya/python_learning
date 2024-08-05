#Solutions assignment 3.1
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