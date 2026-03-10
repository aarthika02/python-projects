import os

#clear screen function
def clear_output():
   os.system('cls' if os.name == 'nt' else 'clear')

#display board
def display_board(board):
   clear_output()
   print(" TIC TAC TOE ")
   print("-------------")
   print(f" {board[7]} | {board[8]} | {board[9]} ")
   print("-------------")
   print(f" {board[4]} | {board[5]} | {board[6]} ")
   print("-------------")
   print(f" {board[1]} | {board[2]} | {board[3]} ")
   print("-------------")

#player chooses marker
def player_input():
   marker = ''
   while marker not in ['X' , 'O']:
       marker = input("Player 1: Choose X or O: ").upper()
   if marker == 'X':
       return ('X','O')
   else:
       return('O','X')

#place marker
def place_marker(board,marker,position):
   board[position] = marker

#check win
def win_check(board,mark):
   return(
       (board[7] == board[8] == board[9] == mark) or
       (board[4] == board[5] == board[6] == mark) or
       (board[1] == board[2] == board[3] == mark) or
       (board[7] == board[4] == board[1] == mark) or
       (board[8] == board[5] == board[2] == mark) or
       (board[9] == board[6] == board[3] == mark) or
       (board[7] == board[5] == board[3] == mark) or
       (board[9] == board[5] == board[1] == mark)
   )

#check space available
def space_check(board,position):
   return board[position] == ' '

#check full board
def full_board_check(board):
   return ' ' not in board[1:]

#player chooses position
def player_choice(board):
   position = 0
   while position not in range(1,10) or not space_check(board,position):
       try:
           position = int(input("choose position(1-9): "))
       except:
           print("Enter a valid number(1-9).")
   return position

#Replay option
def replay():
   return input("Play again? Enter Yes or No: ").lower().startswith('y')

#Game start
print("Welcome to Tic Tac Toe!")

while True:
   board = [' ']*10
   player1_marker, player2_marker = player_input()
   turn = "Player 1"
   game_on = True

   while game_on:
       if turn == "Player 1":
           display_board(board)
           print("Player 1's Turn")
           position = player_choice(board)
           place_marker(board, player1_marker, position)
           if win_check(board, player1_marker):
               display_board(board)
               print("!!!Player 1 Wins!!!")
               game_on = False
           else:
               if full_board_check(board):
                   display_board(board)
                   print("Its a Draw :|")
                   break
               else:
                   turn = "Player 2"

       else:
           display_board(board)
           print("Player 2's Turn")
           position = player_choice(board)
           place_marker(board,player2_marker,position)

           if win_check(board,player2_marker):
               display_board(board)
               print("!!!Player 2 Wins!!!")
               game_on = False
           else:
               if full_board_check(board):
                   display_board(board)
                   print("It's a draw :| ")
                   break
               else:
                   turn = "Player 1"
   if not replay():
       break

print("Thanks for Playing! ")
