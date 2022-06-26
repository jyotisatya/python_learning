# make a ticc tack toe 
# make two player game
# find if one of them is winner
# print winner
# print the borad on every move
#clear   board at the end of game
# make different function for different functionalities lke print board, find if move is valid , 
# find if winner is declared

theboard = {'7' : '' , '8' : '', '9' : '' , 
         '4' : '' , '5' : '' ,'6' : '',
         '1' : '' , '2' : '', '3' : ''}

#board_keys=theboard.getKeys();

def main():
    turn = 'X'
    count = 1;
    while ( count < 10):    
        print_board(theboard)
        print("it's your turn ," + turn + " Move to which place")
        move = str(input())
        ## function to check if move is within 1-9
        if theboard[move] == '':
            turn = 'O' if turn == 'X' else 'X' 
            theboard[move] = turn;
            ## check if the winner is declared and set a flag if its a draw
            count +=1 
        else: 
            print("Already filled") 

        if count == 10:
            print("\nGame Over.\n")                
            print("It's a Tie!!")    
               
def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-+')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-+')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


main();













