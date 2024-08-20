#Add a new field "country" with the value "India" to the address in the user_profile dictionary.
import json

user_profile = {
    "address": {
        "city": "bengaluru",
        "pincode": 560100,
        "state": "karnataka"
    },
    "courses": ["python", "javascript", "java"],
    "name": "jyoti",
    "age": 56,
    "email": "js@example.com"
}


user_profile["address"]["country"] = "India"
print(json.dumps(user_profile,indent=2))