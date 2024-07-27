# Check if a Word Exists**
   # Check if the word 'dog' exists in the `word_meaning_dict` and print its meaning. If the word does not exist,
   #  print a message saying it is not found.

word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
    'banana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,
    'giraffe' : 'a tall African mammal with a very long neck.' ,
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'

}

dict_word = (word_meaning.items())
result=""
for word ,meaning in dict_word:
    if word == 'dog':
        result = meaning
        break
    else:
        result='Not found'

print(result)

#another way to directly search a key in dictionary  
if 'dog' in word_meaning :
    print (f" meaning of 'dog' is : {word_meaning['dog']}")
else:
    print ("not found")    

