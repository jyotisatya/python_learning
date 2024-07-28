# Remove the word 'elephant' from the `word_meaning_dict`. Print the updated dictionary.

import json
word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
   'banana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,
    
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'

}
word_meaning.pop("elephant")

print(json.dumps(word_meaning , indent=2))