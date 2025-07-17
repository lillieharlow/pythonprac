#Create your own simple text-based game

# This game needs to have 1+ function, loop, if/else, break, continue (where suitable), user input

# Game 1: Tic-tac-toe with two users
'''Thoughts:
- 3 x 3 grid with 9 different spots - number the grid 1 - 9
- str = greeting, game over, you won, it's a tie, your turn
- The # of 'win' options is already known - tuple? Add winning combos to tuple?
- Do i need to ask the user if they want to be 'X' or 'O'
- Add .lower() to account for 'x' 'o' - loop back to players turn if input !=
- Board, will need to be printed each time a player makes a move - put in function
- This board will be called multiple times.
- 'X' & 'O' stored in dict. Key used to access and modify numbers when player selects it
- f str place variable inside and variable will come from dict
'''

import os

def draw_board(spots):
  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
  print(board)


def check_turn(turn):
  if turn % 2 == 0: return 'O'
  else: return 'X'

def check_for_win(dict):
  # Handle Horizontal Cases
  if   (spots[1] == spots[2] == spots[3]) \
    or (spots[4] == spots[5] == spots[6]) \
    or (spots[7] == spots[8] == spots[9]):
    return True
  # Handle Vertical Cases
  elif   (spots[1] == spots[4] == spots[7]) \
    or (spots[2] == spots[5] == spots[8]) \
    or (spots[3] == spots[6] == spots[9]):
    return True
  # Diagonal Cases
  elif (spots[1] == spots[5] == spots[9]) \
    or (spots[3] == spots[5] == spots[7]):
    return True
    
  else: return False

# Declare all the variables we're going to need
spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}
playing, complete = True, False
turn = 0
prev_turn = -1
# Game Loop
while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    # Draw the current Game Board
    draw_board(spots)
    # If an invalid turn occurred, let the player know
    if prev_turn == turn:
      print("Invalid spot selected, please pick another.")
    prev_turn = turn
    print("Player " + str((turn % 2) +1 ) + "'s turn: Pick your spot or press q to quit")
    
    # Get input and make sure it's valid
    choice = input()
    # The game has ended, 
    if choice == 'q':
        playing = False
    elif str.isdigit(choice) and int(choice) in spots:
      # Check if the spot is already taken.
      if not spots[int(choice)] in {"X", "O"}:
        # If not, update board and increment the turn
        turn += 1
        spots[int(choice)] = check_turn(turn)
      
    # Check if the game has ended (and if someone won)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False
    
# Update the board one last time. 
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# If there was a winner, say who won
if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else: 
  # Tie Game
  print("No Winner")
  
print("Thanks for playing!") 