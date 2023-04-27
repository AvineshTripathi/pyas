

# Create an empty board with 9 slots
board = [' ' for x in range(9)]

# Define a function to print the current board
def print_board():
  print('   |   |')
  print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
  print('   |   |')

# Define a function to check if the board is full
def is_board_full():
  return ' ' not in board

# Define a function to check if there is a winner
def check_for_winner(symbol):
  # Check rows
  if board[0] == symbol and board[1] == symbol and board[2] == symbol:
    return True
  if board[3] == symbol and board[4] == symbol and board[5] == symbol:
    return True
  if board[6] == symbol and board[7] == symbol and board[8] == symbol:
    return True
  # Check columns
  if board[0] == symbol and board[3] == symbol and board[6] == symbol:
    return True
  if board[1] == symbol and board[4] == symbol and board[7] == symbol:
    return True
  if board[2] == symbol and board[5] == symbol and board[8] == symbol:
    return True
  # Check diagonals
  if board[0] == symbol and board[4] == symbol and board[8] == symbol:
    return True
  if board[2] == symbol and board[4] == symbol and board[6] == symbol:
    return True
  return False

# Define a function to play the game
def play_game():
  print_board()

  while not is_board_full():
    # Player X's turn
    x_choice = int(input("X's turn. Enter a slot number to place X in: "))
    if board[x_choice-1] == ' ':
      board[x_choice-1] = 'X'
      print_board()

      if check_for_winner('X'):
        print("X wins! Congratulations!")
        return
      
    else:
      print("This slot is already taken. Please choose another slot.")
      continue

    # Player O's turn
    o_choice = int(input("O's turn. Enter a slot number to place O in: "))
    if board[o_choice-1] == ' ':
      board[o_choice-1] = 'O'
      print_board()

      if check_for_winner('O'):
        print("O wins! Congratulations!")
        return
      
    else:
      print("This slot is already taken. Please choose another slot.")
      continue

  print("It's a tie!")

# Call the play_game function to start the game
play_game()
