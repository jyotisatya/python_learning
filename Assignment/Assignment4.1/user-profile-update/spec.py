import json
from index import user_update 
from data import user_profile
import unittest
class TestFindMeaning(unittest.TestCase):

    def test_old_city_value_not_exists(self):
        old_city_value = 'bengaluru'
        result = user_update(user_profile,"address", "city", "Bangalore")
        new_city = result['address']['city']
        self.assertNotEqual(old_city_value, new_city , f"Expected {new_city} but got {old_city_value}")

if __name__ == '__main__':
    unittest.main()
