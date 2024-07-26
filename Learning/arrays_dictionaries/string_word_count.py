# importing utility function clean_item from module Util.clean_word.T
# This module is based on folder structure using setup tools which
# converts directory structure in to modules using setup.py in root directory 
from Util.clean_word import clean_item

input_string = """the game of thorne is the best serial and I like this season very much, A man is strong with 
his will and a sword is the ! mighty with its sharpness, is is A special game is sth where you can play hard and fast and that is the ultimate 
game"""

# input list with list of items as given as i/p
word_count = ['a', 'the', 'is','test']

# intialize dictionary
# shorthand initialization word_dic=[word:0 for word in word_count]
# this is intializing dictionary with all the items from list with initial value 0
word_dict={}
for word in word_count:
    word_dict[word]=0

# To loop each words of the string we have converted the string into array split by space 
input_array = input_string.split()

for item in input_array:
    new_item = clean_item(item).lower()

    if new_item in word_dict:
        word_dict[new_item] += 1
    
print(word_dict)

