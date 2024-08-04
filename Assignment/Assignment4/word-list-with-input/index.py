# Find all the words in the 'animals' section that start with the letter 'e'.
 
def find_words(dict,input_section,letter):
    result=[]
    for section, object in dict.items():
        if section == input_section:
            for word  in object:
                if word.startswith(letter):
                    result.append(word)
    return result;               
