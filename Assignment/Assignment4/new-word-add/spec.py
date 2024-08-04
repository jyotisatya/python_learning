from data import iit_syllabus , india ,word_meaning_dict
from index import new_word_addition
import json
import unittest

class TestNewWord(unittest.TestCase):
    
    def test_new_key(self):
      result = new_word_addition(iit_syllabus,"physics","motion",  "this is main dynamics motion")
      self.assertIn("motion", result["physics"])  

    def test_main_key_not_found(self):
        result = new_word_addition(iit_syllabus,"abcd","motion", "this is")
        self.assertNotIn("abcd", result)

    def test_existing_key_update(self):
        result = new_word_addition(india, "Maharashtra", "Pune", "Pune nice") 
        expected = 'Pune nice'
        self.assertEqual(expected,result['Maharashtra']['Pune'],f'Expected {expected} but got {result}' )  

    def test_existing_key_update_negative(self):
        result = new_word_addition(india, "Maharashtra", "Pune", "Pune nice") 
        expected = 'pune nice'
        self.assertNotEqual(expected,result['Maharashtra']['Pune'],f'Expected {expected} but got {result}' )        

        
if __name__ == '__main__':
      unittest.main()




