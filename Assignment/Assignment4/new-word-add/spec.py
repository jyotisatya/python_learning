from data import iit_syllabus , india ,word_meaning_dict
from index import new_word_addition
import json

result = new_word_addition(iit_syllabus,"physics","motion",  "this is main dynamics motion")
print(json.dumps(result, indent=3)
      )