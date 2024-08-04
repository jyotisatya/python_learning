import unittest
from data import word_meaning_dict, iit_syllabus
from index import word_count_dict  

class TestWorldCountDict(unittest.TestCase):

    def test_word_meaning_dict(self):
        result = word_count_dict(word_meaning_dict)
        expected = 16  # Total number of words in word_meaning_dict
        self.assertNotEqual(result, expected, f'Expected {expected} but got {result}')

    def test_iit_syllabus(self):
        result = word_count_dict(iit_syllabus)
        expected = 13  # Total number of words in iit_syllabus
        self.assertEqual(result, expected, f'Expected {expected} but got {result}')

if __name__ == '__main__':
    unittest.main()
