from Util.clean_word import clean_item

input_string = """the game of thorne is the best serial and I like this season very much, A man is strong with 
his will and a sword is the ! mighty with its sharpness, is is A special game is sth where you can play hard and fast and that is the ultimate 
game"""

# Split the input string into words
input_array = input_string.split()

count_a = 0
count_the = 0
count_is = 0

# Iterate over the words and count the occurrences of 'a', 'the', and 'is'
for item in input_array:
    new_item = clean_item(item)
    if new_item.lower() == 'a':
        count_a += 1
    elif new_item.lower() == 'the':
        count_the += 1
    elif new_item.lower() == 'is':
        count_is += 1

print("Count of 'a':", count_a)
print("Count of 'the':", count_the)
print("Count of 'is':", count_is)
