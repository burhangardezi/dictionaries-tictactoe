the_board = {'top-L' :'', 'top-M' : '', 'top-R' : '','mid-L' :'', 'mid-M' : '', 'mid-R' : '',
             'low-L' :'', 'low-M' : '', 'low-R' : ''}

turn = 'X'
def printboard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
for i in range(9):

    printboard(the_board)
    print('Turn of ' + turn + '. Which position to move?' )
    position = input()
    the_board[position] = turn
    if turn == 'X':
        turn = 'Y'
    else:
        turn = 'X'
printboard(the_board)