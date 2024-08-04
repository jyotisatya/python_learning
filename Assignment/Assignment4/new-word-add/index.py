
from typing import Any, Union
# # Write a function to add a new word 'strawberry' with its meaning 'A sweet red fruit' to the 'fruits' section.**
#    - Example: After adding, `word_meaning_dict['fruits']` should include `'strawberry': 'A sweet red fruit'`.

def new_word_addition(input_dict : dict, main_key: str, update_key :  str, update_value : Union[str, dict, list, tuple, int, float, bool]):
    for key , value in input_dict.items():
        if isinstance (value, dict):
            if key == main_key:
                input_dict[main_key].update({update_key:update_value})
                break
    return input_dict
            

