
def pallindrome(str):
    reverse_string = str[ ::-1 ]
    if str == reverse_string:
        return True
    else:
        return False    
    

def main():
    print('Enter a string')
    str = input()
    updated_string = pallindrome(str) 
    if updated_string:
        print('string is pallindrome')
    else:
        print('string is not pallindrome')    

main()    