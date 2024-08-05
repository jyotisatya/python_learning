
from index import user_update 
from data import user_profile
import unittest
class TestFindMeaning(unittest.TestCase):

    def test_old_city_value_not_exists(self):
        old_city_value = 'bengaluru'
        # result = user_update(user_profile,"address", "city", "Bangalore")
        result  = {
        "address" : {
            "city": "Bangalore",
            "pincode" : 560100,
            "state" : "karnataka"
        },
        "courses" : [ "python", "javascript", "java"],
        "name" : "jyoti",
        "age" : 56,
        "email" : "js@example.com"
   }
        self.assertNotEqual(old_city_value, result['city'])

        

if __name__ == '__main__':
    unittest.main()
