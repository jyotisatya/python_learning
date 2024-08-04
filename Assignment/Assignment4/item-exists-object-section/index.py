# Write a function to check if 'notebook' exists in the 'objects' section.

def find_meaning(dict,keyword, input_section):
    flag = False
    for section , object in dict.items():
        if section ==  input_section:
            flag = keyword in object
    return flag        

