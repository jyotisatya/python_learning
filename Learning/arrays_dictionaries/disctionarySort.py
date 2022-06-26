#############################################################
def dictionairy():
 # Declare hash function     
 key_value = {}   
 
# Initializing value
 key_value["Rahul"] = 56      
 key_value["Jyoti"] = 2
 key_value["Atul"] = 12
 key_value["Banar"] = 24
 key_value["Kudbuddi"] = 18     
 key_value[76] = 323
 
 print ("Task 1:-\n");
 print ("Keys are");
  
 a = sorted (key_value.values() ) 

 for i in a:
     print(i)

#############################################################

dictionairy()
