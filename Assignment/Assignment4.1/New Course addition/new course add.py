#Add a new course "HTML" to the courses list in the user_profile dictionary.
user_profile  = {
        "address" : {
            "city": "bengaluru",
            "pincode" : 560100,
            "state" : "karnataka"
        },
        "courses" : [ "python", "javascript", "java"],
        "name" : "jyoti",
        "age" : 56,
        "email" : "js@example.com"
   }
user_profile["courses"].append("HTML")
print(user_profile)