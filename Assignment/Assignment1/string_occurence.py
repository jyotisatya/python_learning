
#store the string to be match in an array
# input enter a string
#break the  input string
#match the input string [i[ with matching string [j]

print('Enter a string')
#str= input() ## jyoti was jyo

str= 'jyoti jyo jyo'

print('Enter Substring')
# sub_string = input() ## jyo
sub_string = 'jyo'


count = 0;
i=0
for i in range(len(str)):
    for j in range(0,len(sub_string)):
        if str[i]==sub_string[j]:
            i=i+1
        else:
            break
    if(j == len(sub_string)-1):
        count=count+1

print(count)