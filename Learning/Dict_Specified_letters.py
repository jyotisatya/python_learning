import json
word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
   'anana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,
    'ppiraffe' : 'a tall African mammal with a very long neck.' ,
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'

}

# create a blank dictionary that will store the result

dict_word = (word_meaning.items())
#print(dict_word)
result_dict={}
for word , meaning in dict_word:
    if word[0] in ['a', 'd' , 'p']:
      result_dict[word] = meaning
print( json.dumps(result_dict,indent=2))        