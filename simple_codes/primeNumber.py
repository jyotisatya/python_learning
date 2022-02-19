import math;
import datetime
input = 10619863;

def if_is_even(x):
    return True if x%2==0 else False

def is_number_prime_function(x):
    
    flag = True;
    if(if_is_even(x)):
        return "Not a prime Number";
    else:   
        n = int(math.sqrt(x));
        for i in range(2, n + 1):
            if(x%i==0):
                flag = False;
                break
            i=i+2;    
    if(flag):
        return "Number is prime Number";
    else:
        return "Not a prime Number";
 
start = datetime.datetime.now();
output=is_number_prime_function(input);
end = datetime.datetime.now();
print ( end - start);
print (output);


