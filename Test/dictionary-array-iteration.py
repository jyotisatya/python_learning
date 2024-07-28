word_meaning_dict = {
    'apple': 'A sweet fruit.',
    'banana': 'A long, yellow fruit.',
    'cat': 'A small domesticated mammal.',
    'dog': 'A loyal domestic animal, often kept as a pet.',
    'elephant': 'A large mammal with a trunk, native to Africa and Asia.',
    'giraffe': 'A tall African mammal with a very long neck and distinctive spots.',
    'house': 'A building where people live, typically a family or group.',
    'ice': 'Frozen water, used to cool drinks and preserve food.',
    'jungle': 'A dense, tropical forest with a rich variety of wildlife and vegetation.',
    'kite': 'A lightweight frame covered with material, flown in the wind at the end of a long string.',
    'lion': 'A large wild cat known as the king of the jungle, with a mane and powerful build.',
    'mountain': 'A natural elevation of the earth’s surface, often with a peak, that is significantly higher than the surrounding terrain.',
    'notebook': 'A book of blank pages for writing notes, recording information, or drawing sketches.',
    'ocean': 'A vast body of salt water that covers almost three-quarters of the Earth’s surface.',
    'pencil': 'A writing instrument with a thin stick of graphite or a similar substance, encased in wood or plastic.'
}

# Print the dictionary
import json



# Task 1 find all the words whose meaning contains  between 6-9  words : create new dictionary, 3-8,12-16
new_dict={}
dict=word_meaning_dict.items()
# print(dict)
for key , value in dict:
    input_array=value.split()
    
    print (len(input_array))
    # if (len(input_array) >= 2 and len(input_array)<= 4 ) or (len(input_array)>=12 and len(input_array)<=16):
    if (len(input_array) in range(3,5)) or(len(input_array) in range(12,17)):
        new_dict[key]=value    
    
print(json.dumps(new_dict , indent=2))  
