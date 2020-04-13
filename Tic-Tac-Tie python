from random import randrange

def DisplayBoard(board):
    for i in range(4):
        print('+', '+', "+", '+', sep='-------')
        if i == 3:
            break
        print("|", "|", "|", "|", sep='       ')
        for j in range(3):
            print('|', board[i][j], '', sep='   ', end='')
        print('|')
        print("|", "|", "|", "|", sep='       ')

def EnterMove(board):
    a = True
    while a:
        move = int(input('Enter your move: '))
        for i in range(len(board)):
            if move in board[i]:
                board[i][board[i].index(move)] = 'O'
                a = False
            elif i == len(board)-1 and move not in board:
               continue
    return board



def MakeListOfFreeFields(board):
    busy_fields1 = []
    busy_fields2 = []
    free_fields = []
    for i in range(len(board)):
        for j in (board[i]):
            if str(j) not in 'XO':
                busy_fields1.append(i)
                busy_fields2.append((board[i].index(j)))
        free_fields = list(zip(busy_fields1, busy_fields2))
    return free_fields


def VictoryFor(board, sign):

    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == sign:
                count += 1
            elif board[i][j] != sign:
                count = 0
        if count == 3:
            print(sign, 'WINS1')
            return sign


    count1 = 0
    for j in range(len(board)):
        for i in range(len(board[j])):
            if board[i][j] == sign:
                count1 += 1
            elif board[i][j] != sign:
                count1 = 0
        if count1 == 3:
            print(sign, 'WINS2')
            return sign

    count2 = 0
    m = len(board)
    for i in range(len(board)):

        if board[i][i] == sign:
            count2 += 1
        elif board[i][i] != sign:
            count2 = 0
        elif board[i][m-1] == sign:
            count2 +=1
            m -= 1
        if count2 == 3:
            print(sign, 'WINS3')
            return sign


    free_list1 = MakeListOfFreeFields(board)
    global message
    message= "TIE"
    if free_list1 == [] and count !=3 and count1 !=3 and count2 !=3:
        return


    if free_list1 != [] and (count == 3 or count1 == 3 or count2 == 3):
        return sign


def DrawMove(board):
    a = True
    while a:
        ramdom = randrange(1, 10)
        for i in range(len(board)):
            if ramdom in board[i]:
                board[i][board[i].index(ramdom)] = 'X'
                a = False
            else:
                continue
    return board



board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'
DisplayBoard(board)

while MakeListOfFreeFields(board) != []:
    EnterMove(board)
    DisplayBoard(board)
    check_winner_X = VictoryFor(board, 'X')
    check_winner_O = VictoryFor(board, 'O')
    if check_winner_X == 'X':
        break
    elif check_winner_O == 'O':
        break
    elif MakeListOfFreeFields(board) == []:
        print(message)
        break

    DrawMove(board)
    DisplayBoard(board)
    check_winner_X = VictoryFor(board, 'X')
    check_winner_O = VictoryFor(board, 'O')
    if check_winner_X == 'X':
        break
    elif check_winner_O == 'O':
        break
    elif MakeListOfFreeFields(board) == []:
        print(message)
        break




