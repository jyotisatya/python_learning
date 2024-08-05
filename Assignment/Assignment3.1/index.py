
from data import input_dict
import json

# # Print the value of "float_value" from nested_dict
# print(input_dict['level1'] ['level2']['level3']['float_value'])


# #Print the value of "str_value" from nested_dict.
# print(input_dict['level1']['level2']['level3']['str_value'])

# #Print the value of the third element in the list_value
# print(input_dict["level1"]["level2"]["level3"]["list_value"][2])

# #Print the value of "bool_value" from nested_dict.
# print(input_dict['level1']['level2']['level3']['bool_value'])

# #Print the value of "name" for the first dictionary inside
# #  the "nested_list".
print(input_dict['level1']['level2']['another_level3']['nested_list'][0]['name'])

# #Print the value of "age" for the second dictionary inside the "nested_list"
print(input_dict['level1']['level2']['another_level3']['nested_list'][1]['age'])

# # Print the value of "key1" from the nested dictionary inside "another_level3"
print(input_dict['level1']['level2']['another_level3']['nested_dict']['key1'])

# #Print the value of the first element in the "simple_list".
print(input_dict['level1']['simple_list'][0])

# #Print the value of "keyA" from "simple_dict".
print(input_dict['level1']['simple_dict']['keyA'])

# #Print the value of "simple_float" from nested_dict.
print(input_dict['simple_float'])

# #Print the value of "simple_str" from nested_dict.
print(input_dict['simple_str'])

# #Print the value of "int_value" from nested_dict.
print(input_dict['level1']['level2']['level3']['int_value'])

# #Print the second element of the list_value.
print(input_dict['level1']['level2']['level3']['list_value'][1])

# #Change the "str_value" to "Hello, World!".
# input_dict['level1']['level2']['level3']['str_value'] = "Hello ,World"
#print(input_dict)

# input_dict['level1']['level2']['level3'].update({"str_value": "Hello,World"})
#print(input_dict)

 #Add a new element to the list_value

input_dict['level1']['level2']['level3']['list_value'].append(5)
#print(input_dict)

#Add a new key-value pair to nested_dict["level1"]["simple_dict"].

input_dict['level1']['simple_dict']['new_key'] = "new_value"


# Remove the key "simple_int" from nested_dict
del input_dict['simple_int']
#print(json.dumps(input_dict,indent =2))

#Write a loop to print all keys and values in nested_dict["level1"]["simple_dict"]

for key , value in input_dict['level1']['simple_dict'].items():
    print("key" , key)
    print("value",value)





