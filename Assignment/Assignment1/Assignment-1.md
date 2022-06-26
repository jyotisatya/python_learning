- Write a function which replace all the vowels from the string and replace with a  '-'.

- Write a function to find if the string is palanderomic or not
example: moon -> No
maam -> Yes

- Iterate the string in python


- Write a function to find all the occurence of a given string.
Example: 
input = 'aabcheedaabdg htyee aabhhtteettaabee bbe aa b"
text = 'aab'
How many 'aab' are there in the given input string?


tree is treatrare

tre 
tree
tr



Solution for 3:

<code>
count = 0
i=0
while i < len(str):
    for j in range(0, len(sub_string)):
        if(str[i] == sub_string[j]):
            j=j+1 
            i=i+1
        else:
            j=0 ## optional just to show sub string iteration is again started
            i=i+1
            break;
        if(j == len(sub_string)):
            count = count + 1    


Final


count = 0;
i=0

while i < len(str):
    for j in range(0, len(sub_string)):
        i += 1 
        if(str[i-1] == sub_string[j]):
            j += 1 
        else:
            break;   
        if(j == len(sub_string)):
            count += 1    

print(count)
</code>