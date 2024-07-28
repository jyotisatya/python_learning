import json
word_meaning_dict = {
    'apple': 'a fruit that is typically round and red, green, or yellow.',
    'banana': 'a long curved fruit that has a thick skin and soft flesh.',
    'cat': 'a small domesticated carnivorous mammal with soft fur.',
    'dog': 'a domesticated carnivorous mammal that typically has a long snout.',
    'elephant': 'a large herbivorous mammal with a trunk.'
}

counter = 0
result = {}
for alpha in word_meaning_dict.items():
    result = { alpha[0]: alpha[1]}
    counter = counter + 1
    if counter == 3:
        break

print (json.dumps(result, indent=2))

counter2 = 0
result2 = {}
for key, value in word_meaning_dict.items():
    result2 = { key: value}
    counter2 = counter2 + 1
    if counter2 == 3:
        break

print (json.dumps(result2, indent=2))