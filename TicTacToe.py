
def clear():
    print("\n")

def switch(player1):
    if player1 == 'X' or player1 == 'x':
        return 'O'
    else:
        return 'X'

def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #btm row
    (board[4] == mark and board[5] == mark and board[6] == mark) or #mid row
    (board[7] == mark and board[8] == mark and board[9] == mark) or #top row
    (board[7] == mark and board[4] == mark and board[1] == mark) or  # left col
    (board[8] == mark and board[5] == mark and board[2] == mark) or  # mid col
    (board[9] == mark and board[6] == mark and board[3] == mark) or  # right col
    (board[1] == mark and board[5] == mark and board[9] == mark) or  # diag2
    (board[7] == mark and board[5] == mark and board[3] == mark))# diag1

def player_input():
    marker = input("Player 1!! Pick one 'X' or 'O' : ").upper()
    if marker == 'X':
        return ('X')
    else:
        return ('O')

def space_check(board,position):
    return board[position] == ' '

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def play_again():
    choice = input("Do you want to play again? Enter 'Yes' or 'No': ").lower()
    return choice=='yes'

test_board = ['#', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X']
game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
new_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def display_board(board):
    clear()
    print("      |     |   ")
    print("   " + board[7] + "  |  " + board[8] + "  |  " + board[9])
    print("------|-----|------")
    print("   " + board[4] + "  |  " + board[5] + "  |  " + board[6])
    print("------|-----|------")
    print("   " + board[1] + "  |  " + board[2] + "  |  " + board[3])
    print("      |     |   ")

player1 = player_input()
while True:
    position = int(input("\nPlease enter position (1-9): "))
    if space_check(game_board,position):
        game_board[position] = player1
    else:
        print("This position is already filled. Choose another position.")
        continue
    display_board(game_board)

    if win_check(game_board, player1):
        print("\nCongratulation {}!!!".format(player1))
        if play_again():
            game_board = new_board
            player1 = player_input()
            continue
        else:
            break
    if full_check(game_board):
        print("The game is tied. GG")
        if play_again():
            game_board=new_board
            player1 = player_input()
            continue
        else:
            break

    player1 = switch(player1)

