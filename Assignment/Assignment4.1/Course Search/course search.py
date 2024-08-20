# Check if the user is enrolled in the "python" course.
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
if 'courses' in user_profile.keys() and 'python' in  user_profile['courses']:
        print('User is enrolled for python')
else:
        print('not enrolled')