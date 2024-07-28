import json


word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
   'banana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,    
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'
}
#result={}
# dict_word=word_meaning.items()
# text = 'is'
# for word, meaning in dict_word:
#     if text in meaning:
#         result[word]= meaning

result = {key : value for key , value in word_meaning.items() if 'is' in value }
print(json.dumps(result , indent=2))        

