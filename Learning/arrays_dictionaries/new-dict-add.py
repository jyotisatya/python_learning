# Add the word 'giraffe' with the meaning 'a tall African mammal with a very long neck' to the 
# `word_meaning_dict`. Print the updated dictionary

word_meaning = {
    'apple' : 'a fruit that is typically round and red, green, or yellow.',
   'banana' : 'a long curved fruit that has a thick skin and soft flesh.' ,
    'cat' : ' small domesticated carnivorous mammal with soft fur.' ,
    'dog' : 'a domesticated carnivorous mammal that typically has a long snout.' ,
    'elephant' : 'a large herbivorous mammal with a trunk.' ,
    
    'house' : 'a building for human habitation, especially one that is lived in by a family or small group of people.'

}
#word_meaning.update ({'giraffe':' tall African mammal with a very long neck'})
#print(word_meaning)

# way of inserting key value at run time
new_word=input('ENter the key:')
new_meaning=input('Enter the meaning')
word_meaning[new_word] = new_meaning
print(word_meaning)
            