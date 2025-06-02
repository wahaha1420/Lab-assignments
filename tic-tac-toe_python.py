import random
def start():
    a = input("X or O?")
    while (a!="X" and a!="O"):
        print("Invalid response. Choose X or O.\n")
        a = input("X or O?")
    if a == "X":
        b = "O"
    else:
        b="X"
    return a,b
def printRound(round):
    print("########################\n")
    print("##### round {} #########\n".format(round))
    print("########################\n\n")
    return 0

def printBoard(board):
    print("current board:\n")
    print("  0 1 2\n")
    for i in range(3):
        print(i,end=" ")
        for j in range(3):
            print(board[i][j],end=" ")
        print("\n")
    return 0
def checkMove(board, row, col):
    if (row>=0 and row<=2) and (col>=0 and col<=2) and (board[row][col]=="."):
        return True
    else:
        return False

def move(board, sym):
    print("{}'s turn:\n".format(sym))
    row = int(input("What row?"))
    col = int(input("What column?"))
    while not checkMove(board,row,col):
        print("Invalid input.")
        row = int(input("What row?"))
        col = int(input("What column?"))
    char = input("Place {} at row {}, column {}? [y/n]".format(sym, row, col))
    if char == "y":
        print("Move placed!\n")
        board[row][col] =sym
        printBoard(board)
    else:
        move(board, sym)
    return 0

def computerMove(board, sym):
    print("{}'s turn:\n".format(sym))
    while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if checkMove(board,row,col):
            break
    board[row][col] = sym
    print("Computer move registered.\n")
    printBoard(board)
    return 0

def checkWinner(board):
    # horizontal
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]

    # vertical
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '.':
            return board[0][col]

    # Upper left to lower right
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]

    # Upper right to lower left
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]

    return None
def is_draw(board):
    for row in board:
        for cell in row:
            if cell == '.':  
                return False
    return True

def play_game():
    board = [
        [".",".","."],
        [".",".","."],
        [".",".","."],
    ]
    player, computer = start()
    round = 1
    if player =="X":
        while True:
            printRound(round)
            round+=1
            printBoard(board)
            move(board,player)
            if(checkWinner(board)):
                print("player {} win!\n".format(player))
                break
            elif is_draw(board):
                print("It's draw!\n")
                break
            else:
                computerMove(board,computer)
                if(checkWinner(board)):
                    print("player {} win!\n".format(computer))
                    break
                elif is_draw(board):
                    print("It's draw!\n")
                    break
                else:
                    continue
    else:
        while True:
            printRound(round)
            round+=1
            printBoard(board)
            computerMove(board,computer)
            if(checkWinner(board)):
                print("player {} win!\n".format(computer))
                break
            elif is_draw(board):
                print("It's draw!\n")
                break
            else:
                move(board,player)
                if(checkWinner(board)):
                    print("player {} win!\n".format(player))
                    break
                elif is_draw(board):
                    print("It's draw!\n")
                    break
                else:
                    continue


play_game()




        

            

