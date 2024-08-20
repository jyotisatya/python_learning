import json
from operator import index

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
user_profile['email']='ABC'
print(json.dumps(user_profile,indent=2))

