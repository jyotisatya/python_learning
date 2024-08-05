def user_update(input_dict, main_key, update_key, update_value):
    for key , value in input_dict.items():
        if isinstance (value, dict):
            if key == main_key:
                input_dict[key].update({update_key:update_value})
    return input_dict

# result = user_update(user_profile,"address", "city", "Bangalore")  
# print(json.dumps(result , indent=3))          