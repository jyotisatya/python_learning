# spec.py
import unittest
from index import find_meaning
from data import word_meaning_dict

class TestFindMeaning(unittest.TestCase):

    def test_notebook_exists(self):
        self.assertTrue(find_meaning(word_meaning_dict, 'notebook', 'objects'))

    def test_notebook_not_exists(self):
        self.assertFalse(find_meaning(word_meaning_dict, 'notebook', 'animals'))

    def test_ice_exists(self):
        self.assertTrue(find_meaning(word_meaning_dict, 'ice', 'objects'))

    def test_ice_not_exists(self):
        self.assertFalse(find_meaning(word_meaning_dict, 'ice', 'fruits'))

    def test_non_existent_section(self):
        self.assertFalse(find_meaning(word_meaning_dict, 'notebook', 'vehicles'))

    def test_empty_section(self):
        empty_dict = {}
        self.assertFalse(find_meaning(empty_dict, 'notebook', 'objects'))

if __name__ == '__main__':
    unittest.main()
