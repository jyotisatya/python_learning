# Functions & Nested Dictionary

```python
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
        'elion': 'A large wild cat known as the king of the jungle, with a mane and powerful build.'
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
```
   


## Questions

### Started Question

**Make a function to find if the word contains any of letter in the given list**
    - Using the above nested array  find if the word contains any letter in #letters = ['y','z','w','t','q','d','m'] and make a new dictionary with word and section 
    ```
    {
    'apple' : 'fruits',
    'banana' : 'fruits',
    'cat' : 'animal',
    'elephant' : 'animal',
    'giraffe' : 'animal',
    'mountain' : 'places'
    }```




   
## Questions

### Very Easy

1. **Find the total number of sections in the dictionary.**
   - Example: Given the dictionary, the function should return `4`.

2. **List all the keys in the 'fruits' section.**
   - Example: Given the dictionary, the function should return `['apple', 'banana']`.

3. **Write a function to return the meaning of the word 'cat'.**
   - Example: Given the dictionary, the function should return `'A small domesticated mammal.'`.

4. **Write a function to check if 'notebook' exists in the 'objects' section.**
   - Example: Given the dictionary, the function should return `True`.

### Easy

5. **Write a function to count the total number of words in the dictionary.**
   - Example: Given the dictionary, the function should return `12`.

6. **Find all the words in the 'animals' section that start with the letter 'e'.**
   - Example: Given the dictionary, the function should return `['elephant']`.

7. **Write a function to add a new word 'strawberry' with its meaning 'A sweet red fruit' to the 'fruits' section.**
   - Example: After adding, `word_meaning_dict['fruits']` should include `'strawberry': 'A sweet red fruit'`.
   -  another question with separate input data:
   this data will include a nested dictionary of list and dict
   ```python 
   user_profile  = {
        "address" : {
            "city": "bengaluru",
            "pincode" : 560100,
            "state" : "karnataka"
        },
        "courses" : [ "python", "javascript", "java"],
        "name" : "jyoti",
        "age" : 56,
        "email" : "js@example.com"
   }
   ```
   CHeck more questions in assignment 4.1


8. **Write a function to delete the word 'lion' from the 'animals' section.**
   - Example: After deletion, `word_meaning_dict['animals']` should not include the key `'lion'`.

9. **Find all words in the 'places' section with more than 6 characters.**
   - Example: Given the dictionary, the function should return `['mountain', 'jungle']`.

10. **Write a function to update the meaning of 'dog' to 'A loyal pet, often considered as man’s best friend'.**
    - Example: After updating, `word_meaning_dict['animals']['dog']` should be `'A loyal pet, often considered as man’s best friend'`.

### Medium

11. **Create a function to return all words and their meanings in a given section.**
    - Example: For the 'fruits' section, the function should return `{'apple': 'A sweet fruit.', 'banana': 'A long, yellow fruit.'}`.

12. **Write a function to find all sections that contain words with the letter 'e'.**
    - Example: Given the dictionary, the function should return `['animals', 'places']`.

13. **Write a function to return a list of all words in the dictionary.**
    - Example: Given the dictionary, the function should return `['apple', 'banana', 'cat', 'dog', 'elephant', 'giraffe', 'lion', 'house', 'mountain', 'ocean', 'jungle', 'ice', 'kite', 'notebook', 'pencil']`.

14. **Create a function to merge two sections into one, e.g., merge 'fruits' and 'objects' into 'items'.**
    - Example: After merging, `word_meaning_dict['items']` should include all words from both 'fruits' and 'objects'.

15. **Write a function to count the total number of letters in all words in the dictionary.**
    - Example: Given the dictionary, the function should return the total count of letters in all the words.

16. **Create a function to find the section with the longest word.**
    - Example: Given the dictionary, the function should return `'animals'`.

### Hard

17. **Write a function to reverse the meanings of all words in the dictionary.**
    - Example: For the 'cat' in the 'animals' section, the meaning should become '.lammed detacitsemod llamS A'.

18. **Create a function to swap two sections in the dictionary.**
    - Example: After swapping 'fruits' and 'animals', `word_meaning_dict['fruits']` should contain all words from the 'animals' section and vice versa.

19. **Write a function to find the top 3 sections with the most words.**
    - Example: Given the dictionary, the function should return the top 3 sections by word count.

### Very Hard

20. **Create a function to flatten the dictionary into a list of tuples, where each tuple contains a word and its meaning.**
    - Example: Given the dictionary, the function should return `[('apple', 'A sweet fruit.'), ('banana', 'A long, yellow fruit.'), ('cat', 'A small domesticated mammal.'), ...]`.
