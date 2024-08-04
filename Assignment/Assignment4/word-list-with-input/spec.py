import unittest
from testdata import word_meaning_dict
from index import find_words

class TestWordListWithInput (unittest.TestCase):

    def test_animal_has_e(self):
        expected_result = ['elephant']
        actual_result= find_words(word_meaning_dict,'animals','e' )
        self.assertEqual(actual_result,expected_result,f'Expected {expected_result} got {actual_result}')
        
if __name__ == '__main__':
    unittest.main()