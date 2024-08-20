import json

#Remove the course "java" from the courses list in the user_profile dictionary.

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
user_profile["courses"].remove("java")
print(json.dumps(user_profile,indent=2))