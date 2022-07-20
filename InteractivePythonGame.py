import os #Clean up the console
import time
import random

def space(string, length):
  #Function to create spaces in the console
  for i in range(0, length):
    print(string)
    print(string)

def welcome():#Welcome Screen
  print("* WELCOME TO GAMING APP *")
  space("",5)
  input("* Press ENTER key to START *")
  os.system("clear") # Clean old output from the console
  option()#Next Function
  
def option():#Choose the game
  space("*", 5)
  print("1) Rock Paper Scissors\n2) Tic Tac Toe\n3) Hangman\n4) Connect4")
  space("*", 5)
  print("Enter the number #")
  choice = int(input("Which game would you like to play?"))
  space(" ", 2)
  if choice == 1:
    rockpaperscissors()#RPS game
  elif choice == 2:
    tictactoemenu()#Tic tac toe mode selection
  elif choice == 3:
    hangman()#Hangman Game
  elif choice == 4:
    connect4()#Connect 4 game
  else:
    print("No such number #")
    welcome()
    
def rockpaperscissors():
  print("* ROCK, PAPER, SCISSORS *")
  print("You wil be competing against computer")
  print("The competitor who first scores 5 points will be declared as the winner")
  print("For Rock, Enter 0")
  print("For Paper, Enter 1")
  print("For Scissors, Enter 2")
  print("To EndGame and return to main MainMenu, Enter -1")
  #Game Variables
  player_score = 0
  bot_score = 0
  game_rounds = 0
  game_options = ["Rock","Paper","Scissors"]
  #Game Loop
  while player_score < 5 and bot_score < 5 and game_rounds < 25:
    game_rounds += 1
    player_option = int(input("Enter play option number: "))
    space("*", 3)
    if player_option == -1:
      print("Thank you for playing")
      welcome()#Send him back to welcome screen
      break
    bot_option = random.choice([0 ,1 ,2 ]) #Choose computer play option
    if player_option == bot_option:
      print("Tie")
    elif player_option == 0 and bot_option == 1: #Rock vs Paper
      bot_score += 1
    elif player_option == 0 and bot_option == 2: #Rock vs Scissors
      player_score += 1
    elif player_option == 1 and bot_option == 0: #Paper vs Rock
      player_score += 1
    elif player_option == 1 and bot_option == 2: #Paper vs Scissors
      bot_score += 1
    elif player_option == 2 and bot_option == 1: #Scissors vs Paper
      player_score += 1
    elif player_option == 2 and bot_option == 0: #Scissors vs Rock
      bot_score += 1
    print("You: ", game_options[player_option]) 
    print("Computer: ", game_options[bot_option])
    print("Scores")
    print("You= ", player_score, "\t Computer= ", bot_score)
    space("*", 3)
    if(player_score > bot_score and player_score == 5):
      print("Congratulations! You are the winner!")
      option()
    elif (bot_score > player_score and bot_score == 5):
      print("Sorry! Better luck next time!")
      option()
    elif(player_score == bot_score and game_rounds >= 25):
      print("It's a draw!")
      option()
      
def tictactoemenu():
  print("Welcome to Tic Tac Toe game")
  space("*", 4)
  print("1) Single Player(No Friends Mode)\n2) Two Player(Friends Mode)")
  space("*", 4)
  choice = int(input("Enter your choice number: "))
  if choice == 1:
    single_player()
  elif choice == 2:
    two_player()
  else:
    print("Invalid Input")
    tictactoemenu()
    
def two_player():
  board = [""," "," "," "," "," "," "," "," "," "]
  
  def rules():
    print("Welcome to Tic Tac Toe game")
    print("This is a two player game where Player 1 is X and Player 2 is O")
    print("Enter choice from 1 to 9")
    print("""
        1 | 2 | 3
       ---|---|---
        4 | 5 | 6
       ---|---|---
        7 | 8 | 9
    """)
  
  def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")
    
  def is_winner(board, player): #Check for the win
    if (board[1] == player and board[2] == player and board[3] == player) or \
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
      
  #Check for a tie
  def is_board_full(board):
    if " " in board: #Check if there are any empty space left
      return False
    else:
      return True
      
  #Game Loop
  while True:
    os.system("clear")
    rules()
    print_board()
    
    #Player 1
    while True:
      choice = int(input("Please choose an empty spot for X: "))
      if board[choice] == " ":#Check if spot is empty
        board[choice] = "X"
        break  
      else:
        print("Spot Already Taken")
        time.sleep(1)
    #Check for player 1 win
    if is_winner(board, "X"):
      os.system("clear")
      rules()
      print_board()
      print("Player 1 wins!")
      input("Press ENTER to Continue")
      os.system("clear")
      option()
      break
    
    os.system("clear")
    rules()
    print_board()
    
    #Check if board is full, check for tie
    if is_board_full(board):
      print("Tie")
      break
      input("Press Enter to continue")
      option()
      
    #Player 2
    while True:
      choice = int(input("Please choose an empty spot for O: "))
      if board[choice] == " ":#Check if spot is empty
        board[choice] = "O"
        break  
      else:
        print("Spot Already Taken")
        time.sleep(1)
    #Check for player 1 win
    if is_winner(board, "O"):
      os.system("clear")
      rules()
      print_board()
      print("Player 2 wins!")
      input("Press ENTER to Continue")
      os.system("clear")
      option()
      break
    
    os.system("clear")
    rules()
    print_board()
    
    #Check if board is full, check for tie
    if is_board_full(board):
      print("Tie")
      break
      input("Press Enter to continue")
      option()
    
def single_player():
  board = [""," "," "," "," "," "," "," "," "," "]
  
  def rules():
    print("Welcome to Tic Tac Toe game")
    print("This is a Single Player No Friend experience, where Player 1 is X and Computer is O")
    print("Enter choice from 1 to 9")
    print("""
        1 | 2 | 3
       ---|---|---
        4 | 5 | 6
       ---|---|---
        7 | 8 | 9
    """)
  
  def print_board():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")
    
  def is_winner(board, player): #Check for the win
    if (board[1] == player and board[2] == player and board[3] == player) or \
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
      
  #Check for a tie
  def is_board_full(board):
    if " " in board: #Check if there are any empty space left
      return False
    else:
      return True  
      
  #Enemy AI
  def get_computer_move(board, player):
    #check for a win
    for i in range(1, 10):
      if board[i] == " ":#Check if any empty spaces left
        board[i] = player#If there is no spaces left, game will be a tie
        if is_winner(board, player): #For as long as there are empty spaces
          return i #Check if player won the game
        else:
          board[i] = " "
    
    #Check for column block
    for i in [1,2,3]:
      if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
        return i+6 #Put O at the end of the column
      if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
        return i#Put O at the beginning of the column
      if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
        return i#Put O in the middle of the column
        
    #Check for Row block
    for i in [1,4,7]:
      if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
        return i+2 #Put O at the end of the row
      if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
        return i#Put O at the beginning of the row
      if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
        return i#Put O in the middle of the row
        
    #Check for diagnol block
    if board[1] == "X" and board[5] == "X" and board[9] == " ":
      return 9
    if board[9] == "X" and board[5] == "X" and board[1] == " ":
      return 1
    if board[1] == "X" and board[9] == "X" and board[5] == " ":
      return 5
    if board[3] == "X" and board[5] == "X" and board[7] == " ":
      return 7
    if board[7] == "X" and board[5] == "X" and board[3] == " ":
      return 3
    if board[3] == "X" and board[7] == "X" and board[5] == " ":
      return 5
      
    if board[5] == " ": #Check if user didnt take middle spot
      return 5
    while True:
      move = random.randint(1, 9)
      if board[move] == " ":
        return move
        break
      
  #Game Loop
  while True:
    os.system("clear")
    rules()
    print_board()
    
    #Player 1
    while True:
      choice = int(input("Please choose an empty spot for X: "))
      if board[choice] == " ":#Check if spot is empty
        board[choice] = "X"
        break  
      else:
        print("Spot Already Taken")
        time.sleep(1)
    #Check for player 1 win
    if is_winner(board, "X"):
      os.system("clear")
      rules()
      print_board()
      print("Player 1 wins!")
      input("Press ENTER to Continue")
      os.system("clear")
      option()
      break
    
    os.system("clear")
    rules()
    print_board()
    
    #Check if board is full, check for tie
    if is_board_full(board):
      print("Tie")
      break
      input("Press Enter to continue")
      option()
      
    #Computer
    while True:
      choice = get_computer_move(board, "O")
      if board[choice] == " ":#Check if spot is empty
        board[choice] = "O"
        break  
      else:
        print("Spot Already Taken")
        time.sleep(1)
    #Check for computer win
    if is_winner(board, "O"):
      os.system("clear")
      rules()
      print_board()
      print("Computer destroyed you")
      input("Press ENTER to Continue")
      os.system("clear")
      option()
      break
    
    os.system("clear")
    rules()
    print_board()
    
    #Check if board is full, check for tie
    if is_board_full(board):
      print("Tie")
      break
      input("Press Enter to continue")
      option()
      
def hangman():
  HANGMAN = (
    """
   ------
  |     |
  |
  |
  |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |
  |
  |
  |
  |
  ----------
  """
     ,
  """
   ------
  |     |
  |     0
  |     +
  |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |    -+
  |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |    -+-
  |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |   /-+-
  |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |   /-+-/
  |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |   /-+-/
  |     |
  |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |   /-+-/
  |     |
  |     |
  |
  |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |   /-+-/
  |     |
  |     |
  |    |
  |    |
  ----------
  """
      ,
  """
   ------
  |     |
  |     0
  |   /-+-/
  |     |
  |     |
  |    | |
  |    | |
  ----------
  """
  )
  max_wrong = len(HANGMAN) - 1#Max amount of mistakes that player can do
  #Words for guessing
  words = ["OVERUSED", "TUESDAY", "JAVASCRIPT", "CHAMPIONSHIP", "PIRATEBAY", "CODING"]
  #Choose a random word to hide
  hidden = random.choice(words)
  so_far = "-" * len(hidden) #replace letters with dashes and hide the word
  wrong = 0 #Keep track of player's mistakes
  used = [] #Store guessed letters here
  print("Welcome to Hangman. Good Luck, Have Fun")
  #Game Loop
  while wrong < max_wrong and so_far != hidden: #!= stands for 'doesnt equal'
    print(HANGMAN[wrong])
    print("\nYou've used the following letters: " + str(used))
    print("\nSo far, the word is: " + so_far)
    guess = input("\nEnter your guess: ")
    guess = guess.upper()#Turn Lower case into Upper Case
    #Check if guess is already been used
    while guess in used:
      print("You've already guess that letter " + guess)
      guess = input("Try again: ")
      guess = guess.upper()
    used.append(guess)#Store your guess
    #Check if guess is correct
    if guess in hidden:
      print("Yes!" + guess + " is in the word!")
      #create new so_far to include the guess
      #Replace blank space with a correct letter 
      new = ""
      #Loop through the entire word and find the pos of the letter
      for i in range(len(hidden)):
        if guess == hidden[i]:
          new += guess
        else:
          new += so_far[i]
      #this redefines so_far to include the letter guessed
      so_far = new
    #If guess is wrong, print out the following
    else:
      print("\nSorry " + guess + " isn't in the word.")
      wrong += 1
  #If the number of tries reaches the limit, game is over
  #Or if user guesses the word, print the following
  if wrong == max_wrong:
    print(HANGMAN[wrong])
    print("You've been hanged!")
  else:
    print("You've guessed it!")
  print("\nThe word was " + hidden)
  
  
def connect4():
  #Variables
  board = []
  label = []
  whos_turn = 0b10
  winner = False
  last = 0
  column = 0
  boardheight = 6
  boardwidth = 7
  
  #Generate empty board
  def generate_board(boardheight, boardwidth):
    for i in range(8):
      if i < boardheight:
        board.append(["_"] * boardwidth)
      elif i < boardwidth:
        board.append(["^"] * boardwidth)
      else:
        for j in range(boardwidth):
          label.append(str(j+1))#Print numbers under the board
        board.append(label)
        
  def start():
    print("Let's play Connect Four!")
    sequence = ["3", ".", ".", "2", ".", ".", "1", ".", "."]
    for i in sequence:
      time.sleep(0.3333)#Wait 30 miliseconds before printing each item
      print i, #Put comma to print numbers in a row
      
  def print_board(board):
    print ("\n") #Return cursor on the next line
    for row in board:
      print " ".join(row)
    print("\n")
    
  def toggle(turn):
    mask = 0b11
    turn = turn ^ mask#Toggle between player's turns
    print ("It is player's " + str(turn) + " turn")
    return turn
    
  def mark_board(last, column):
    if whos_turn == 0b01:
      board[last][column] = "1"#Player one turn
    else:
      board[last][column] = "2"#Player two turn
    print_board(board)
    
  def play():
    while True:
      try:
        column = int(input("Pick a column (1-7): ")) - 1
        if column >= 1 and column <= boardwidth:
          for i in range(7):
            if board[i][column] == "_":
              last = i
          mark_board(last, column)
        else:
          print("You picked a column outside of the board!")
        break#Finish player's turn
      except:
        print("Not a valid number! Please try again...")
        
  def check_winner(board, player):
    #Check horizontal spaces
    for y in range(boardheight):#Loop through columns
      for x in range(boardwidth - 3):#Loop through rows 
        if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
          return True
          
    #Check vertical spaces
    for y in range(boardwidth):#Loop through columns
      for x in range(boardheight - 3):#Loop through rows 
        if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
          return True
          
    #Check / diagnol spaces
    for y in range(boardwidth - 3):#Loop through columns
      for x in range(3, boardheight):#Loop through rows 
        if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
          return True
          
    #Check \ diagnol spaces
    for y in range(boardwidth - 3):#Loop through columns
      for x in range(boardheight - 3):#Loop through rows 
        if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
          return True
          
    return False
    
  start()
  generate_board(boardheight, boardwidth)
  print_board(board)
  
  #Game Loop
  while winner == False:#Run the game until winner is determined
    whos_turn = toggle(whos_turn) #Toggle between player's turns
    play()
    winner = check_winner(board, str(whos_turn))
  if winner == True:#Check if someone won
    print("Player " + str(whos_turn) + " wins!")
welcome()
    
    
  
  
  
  