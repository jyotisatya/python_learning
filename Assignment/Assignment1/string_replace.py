
def vowel_replace(str , char):
    newstr = ""
    for i in range (len(str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] =='i' or str[i] =='o' or str[i] =='u':
            newstr = newstr + char
        else:
            newstr = newstr + str[i]
    return newstr
    
def main(): 

    print('Enter a string')
    str = input()

    print('Enter a character to replace vowel')
    char = input()
    
    replaced_string = vowel_replace(str ,char)
    
    print('string after modifying',replaced_string) 

main()



    
