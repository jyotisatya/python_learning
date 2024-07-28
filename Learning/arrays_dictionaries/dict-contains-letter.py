# Create a list of all words in `word_meaning_dict` that contain the letter 'a'. Print this list.


import json


word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
   'banana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,    
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'
}

#result= []

#for word in word_meaning: 
   # if word.find('a') > -1: 
       # result.append(word)

# for word in word_meaning:
#     if 'a' in word:
#         result.append(word)

data = [ word for word in word_meaning if 'a' in word ]
print( json.dumps(data,indent=2))

    

