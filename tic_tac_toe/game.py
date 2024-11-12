import random
def display_board(board):
    print (board[1], board[2],board[3])
    print ('------')
    print (board[4],board[5],board[6])
    print ('------')
    print (board[7],board[8],board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
board_map = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# display_board(board_map)

def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Player 1, choose X or O: ").upper()
    print ('Player 1 has chosen: '+ marker)
    if marker == 'X':
        print ('Player 2, you are O')
        return ('X', 'O')
    else: 
        print ('Player 2, you are X')
        return ('O', 'X')

# player_input()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    winning_conditions = False
    while not winning_conditions:
        if (board[1] == board[2] == board[3] == mark):
            print ( mark +' wins! With top row')
            display_board(board)
            winning_conditions = True
        elif (board[4] == board[5] == board[6] == mark):
            print ( mark +' wins! With middle row')
            display_board(board)
            winning_conditions = True
        elif (board[7] == board[8] == board[9] == mark):
            print ( mark +' wins! With bottom row')
            display_board(board)
            winning_conditions = True
        elif (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark):
            print ( mark +' wins! Horizontally')
            display_board(board)
            winning_conditions = True
        else:
            pass
# win_check(test_board,'X')

def choose_first():
    if random.randint(0,1) == 0:
        print ('Player 1 goes first')
        return 'Player 1'
    else:
        print ('Player 2 goes first')
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position: '))
    return position

def replay():
    return input('Do you want to play again? Yes or No: ').lower() == 'yes'

def store_scores(player1_score, player2_score):
    with open('scores.txt', 'a') as f:
        f.write('Player 1 Score:'+ str(player1_score) + '\nPlayer 2 Score:'+ str(player2_score) + '\n')

        

def game_start():
    print('Welcome to Tic Tac Toe!')
    player1_score = 0
    player2_score = 0
    while True:
        game_board = [' '] * 10
        print ("Let's start the game! ")
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print ("Let's start with: " + turn)
        
        rugame = input('Are we ready to play? Yes or No: ')

        if rugame.lower() == 'yes' or rugame.lower() == 'y':
            game_on = True
        else:
            game_on = False
        while game_on:
            display_board(board_map)
            if turn == 'Player 1':
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board, player1_marker, position)
                if win_check(game_board, player1_marker):
                    display_board(game_board)
                    print ('Player 1 wins!')
                    player1_score += 1
                    store_scores(player1_score, player2_score)
                    game_on = False
                elif full_board_check(game_board):
                    display_board(game_board)
                    print ('It\'s a tie!')
                    game_on = False
                else:
                    turn = 'Player 2'
            else:
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board, player1_marker, position)
                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print ('Player 2 wins!')
                    player2_score += 1
                    store_scores(player1_score, player2_score)
                    game_on = False
                elif full_board_check(game_board):
                    display_board(game_board)
                    print ('It\'s a tie!')
                    game_on = False
                else:
                    turn = 'Player 1'
    
        if not replay():
            break

game_start()