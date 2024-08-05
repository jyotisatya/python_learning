# Sample 4-5 level nested dictionary
input_dict = {
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

