
# coding: utf-8

# In[1]:


# Tic Tac Toe

import random
def display_board(board):      # function to display the board

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[2]:


test_board=['o','x','o','x','o','x','o','x','o','x']     # funtion to display the sample board
display_board(test_board)


# In[3]:


def player_input():    # funtion to assign the player's marker
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[4]:


player_input()


# In[5]:


def place_marker(board,marker,position):     # function to take board,marker and position of the marker
    board[position]=marker


# In[6]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[7]:


def win_check(board,mark):    # function to check if a player wins
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[8]:


win_check(test_board,'o')


# In[9]:


import random     # function to choose the player randomly

def choose_first():
    if random.randint(0,1) == 0:
        return 'player2'
    else:
        return 'player1'


# In[10]:


def space_check(board, position):    # function to check if space is freely available
    
    return board[position] == ' '


# In[11]:


def full_board_check(board):         # function to check if board is completely filled
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[12]:


def player_choice(board):       # function that asks player to choose the position
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[ ]:


def reply():                # function that asks player to play the game again
    return input('do you wnt to play the game again? enter yes or no').lower().startswith('y')


# In[ ]:


print('welcome to Tic Tac Toe')

while True:
    theBoard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+ 'will go first')
    
    play_game = input('Are you ready to play the game? Enter yes or no')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        
        
        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                   
                
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

