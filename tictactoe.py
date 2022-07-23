#Tic Tac Toe (2 modes)

import random, os, time

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def start():
    print("Welcome to Tic Tac Toe!")
    print("""
    Choose Game Mode
    1. Single Player
    2. Multiplayer
    """)
    mode = int(input("Enter Game Mode Number: "))

    if mode == 1:
        print("Single Player Chosen")
    elif mode == 2:
        print("Multiplayer Chosen")
        multiplayer()
    else:
        print("Invalid. Enter 1 or 2")
def rules(num_pl):
    if num_pl == 1:
        print("Single Player Tic Tac Toe. Player is X, Bot is O")
    else:
        print("Multiplayer Tic Tac Toe. Player 1 is X, Player 2 is O")
    print("Use numbers 1-9")
    print("""
    1 | 2 | 3
    -- --- --
    4 | 5 | 6
    -- --- --
    7 | 8 | 9
    -- --- --    
    """)

def drawBoard():
    print("   |  |  ")
    print(" " + board[1] + " | " + board[2] + "|  " + board[3])
    print("   |  |  ")
    print("---|--|---")
    print("   |  |  ")
    print(" " + board[4] + " | " + board[5] + "|  " + board[6])
    print("   |  |  ")
    print("---|--|---")
    print("   |  |  ")
    print(" " + board[7] + " | " + board[8] + "|  " + board[9])
    print("   |  |  ")

def isWinner(board, player):
    if(board[1] == player and board[2] == player and board[3] == player) or \
    (board[4] == player and board[5] == player and board[6] == player) or \
    (board[7] == player and board[8] == player and board[9] == player) or \
    (board[1] == player and board[4] == player and board[7] == player) or \
    (board[2] == player and board[5] == player and board[8] == player) or \
    (board[3] == player and board[6] == player and board[9] == player) or \
    (board[1] == player and board[5] == player and board[9] == player) or \
    (board[3] == player and board[5] == player and board[7] == player):
        return True
    else:
        return False

def is_board_full(gridcells):
    if " " in gridcells:
        return False
    else:
        return True

def multiplayer():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    while True:
        os.system("clear")
        rules(2)
        drawBoard()
        while True:
            p1input = int(input("Player X enter grid position: "))
            if p1input > len(board):
                print("Please enter a valid grid number 1 - 9")
            elif p1input == " ":
                board[p1input] = "X"
                break
            else:
                print("Please choose a different position")
        if isWinner(board, "X"):
            os.system("clear")
            rules(2)
            drawBoard()
            print("Player X wins!")
            input("Press Enter to continue")
            start()
            break
        os.system("clear")
        rules(2)
        drawBoard()

        if is_board_full(board):
            print("Game is tied")
            input("Press Enter to continue")
            start()
            break

        while True:
            p2input = int(input("Player O enter grid position: "))
            if p2input > len(board):
                print("Please enter a valid grid number 1 - 9")
            elif p2input == " ":
                board[p2input] = "O"
                break
            else:
                print("Please choose a different position")
        if isWinner(board, "O"):
            os.system("clear")
            rules(2)
            drawBoard()
            print("Player O wins!")
            input("Press Enter to continue")
            start()
            break
        os.system("clear")
        rules(2)
        drawBoard()

        if is_board_full(board):
            print("Game is tied")
            input("Press Enter to continue")
            start()
            break

start()



