

def factorial(n):
    v = 1;
    for i in reversed(range(2,n+1)):
        v = v * i;  
    return v;

print ('Enter a number to print factorial');
n = input();

factorialOfN = factorial(n);
print (factorialOfN)
