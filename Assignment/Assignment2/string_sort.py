print('Enter a string to be sort')
str= input()
list1 = list(str.strip(""))

for i in range(0,len(list1)):
    for j in range(i+1 , len(list1)):
        if(list1[i] > list1[j]):
            list1[i] , list1[j] = list1[j] ,list1[i] 

result = ''.join(list1)

print('String after sorting', result)
