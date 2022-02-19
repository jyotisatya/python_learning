########## PART 1: INPUT #########
print ('Enter szie of an array');
SIZE = input();

# INITIALISE EMPTY ARRAY 
my_array = [];
V = "Enter element" + str(SIZE) +" in array";
print (V);
for i in range(1, SIZE+1):
    my_array.append(input());
print("Your array is: ", my_array)

########### PART 3: LOGIC #########
def sumOfEvenInArray(arr):
    sum = 0;
    for i in arr:
        if(i%2==0):
            sum = sum + i;
    return sum;


########### PART 3: OUTPUT #########
sum = sumOfEvenInArray(my_array)

print("Final: ", sum)