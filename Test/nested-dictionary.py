import json


word_meaning_dict = {
    'fruits': {
        'apple': 'A sweet fruit.',
        'banana': 'A long, yellow fruit.'
    },
    'animals': {
        'cat': 'A small domesticated mammal.',
        'dog': 'A loyal domestic animal, often kept as a pet.',
        'elephant': 'A large mammal with a trunk, native to Africa and Asia.',
        'giraffe': 'A tall African mammal with a very long neck and distinctive spots.',
        'lion': 'A large wild cat known as the king of the jungle, with a mane and powerful build.'
    },
    'places': {
        'house': 'A building where people live, typically a family or group.',
        'mountain': 'A natural elevation of the earth’s surface, often with a peak, that is significantly higher than the surrounding terrain.',
        'ocean': 'A vast body of salt water that covers almost three-quarters of the Earth’s surface.',
        'jungle': 'A dense, tropical forest with a rich variety of wildlife and vegetation.'
    },
    'objects': {
        'icae': 'Frozen water, used to cool drinks and preserve food.',
        'kite': 'A lightweight frame covered with material, flown in the wind at the end of a long string.',
        'notebook': 'A book of blank pages for writing notes, recording information, or drawing sketches.',
        'pencil': 'A writing instrument with a thin stick of graphite or a similar substance, encased in wood or plastic.'
    }
}

# Print the nested dictionary

result_t1 = {}
result_t2={}
#letters = ['y','z','w','t','q','d','m']

for section, word_meaning in word_meaning_dict.items():
   result_t1[section.upper()]= len(word_meaning)
   for word , meaning in word_meaning.items():
      if ('y' in word) or ('p' in word):
         result_t2[word]=section
     
     


print(json.dumps(result_t2, indent=2))   







# make a new dictionary and find the number of words in each section and make each section in upper case

'''
{
    FRUITS: 2,
    ANIMALS: 5,
    PLACES: 4
    OBJECTS: 4
}
'''

# Make an dictionary where word contains a letter given 'a' and print the words and value as its section

'''
{
    'apple' : 'fruits',
    'banana' : 'fruits',
    'cat' : 'animal',
    'elephant' : 'animal',
    'giraffe' : 'animal',
    'mountain' : 'places'
 }

'''