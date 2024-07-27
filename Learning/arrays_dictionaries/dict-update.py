# Update the meaning of the word 'apple' to 'a round fruit with red, green, or yellow skin'. Print the updated dictionary


import json


word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
   'banana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,
    
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'

}

# word_meaning.update({'nest' : 'round fruit with red, green, or yellow skin'})

word = 'apple'
value = 'new value'
try:
    if word in word_meaning:
        word_meaning[word] = value
    else:
        raise KeyError(f"Key '{word}' does not exist in the dictionary.")
except KeyError as e:
    print(e)


# print(json.dumps( word_meaning, indent=2))

