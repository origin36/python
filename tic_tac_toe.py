# utf-8

"""
my version of the classic tic tac toe game.
"""

loc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
markers = ('X', 'O')


def ready_bool(ready):
    """takes a user input string as an argument and returns a boolean value."""
    if ready.lower() == 'y':
        return True
    else:
        return False


def get_player2_mark(p1_mark):
    """assigns a marker to a numeric user input value."""
    if p1_mark == 2:
        return markers[0]
    else:
        return markers[1]


def update_board(player1_spot, player2_spot):
    """updates the locations with the marker."""
    if player1_spot == -1:
        loc[player2_spot - 1] = player2_mark
    else:
        loc[player1_spot - 1] = player1_mark


def check_win():
    """checks to see if any of the win conditions are met."""
    for mark in markers:
        if loc[0] == mark and loc[1] == mark and loc[2] == mark:
            return True
        if loc[0] == mark and loc[3] == mark and loc[6] == mark:
            return True
        if loc[0] == mark and loc[4] == mark and loc[8] == mark:
            return True
        if loc[1] == mark and loc[4] == mark and loc[7] == mark:
            return True
        if loc[2] == mark and loc[4] == mark and loc[6] == mark:
            return True
        if loc[2] == mark and loc[5] == mark and loc[8] == mark:
            return True
        if loc[3] == mark and loc[4] == mark and loc[5] == mark:
            return True
        if loc[6] == mark and loc[7] == mark and loc[8] == mark:
            return True
        else:
            return False


def triple_hash():
    """prints 3 lines of hash marks to make the board."""
    board_format_1 = '                                              #                     #'
    print(board_format_1,'\n',board_format_1,'\n',board_format_1,'\n',board_format_1,sep='')


def show_board(player_name='player',win=False):
    """prints the board with corresponding locations from loc string.  takes 2 args."""
    print('\n'*10)
    triple_hash();
    print(f'                                   {loc[0]}          #          {loc[1]}          #       {loc[2]}')
    triple_hash()
    print('                         #################################################################')
    triple_hash()
    print(f'                                   {loc[3]}          #          {loc[4]}          #       {loc[5]}')
    triple_hash()
    print('                         #################################################################')
    triple_hash()
    print(f'                                   {loc[6]}          #          {loc[7]}          #       {loc[8]}')
    triple_hash()

    if win:
        print(f'\n\ncongratulations, {player_name}, you have won!')


print('welcome to tic tac toe.')
print('player 1, enter your name:')
p1_name = input()

print('player 2, enter your name:')
p2_name = input() # assign name to player 2

print(f'{p1_name}, choose: 1 = {markers[0]} or 2 = {markers[1]}')
player1_mark_int = int(input())
player1_mark = markers[player1_mark_int-1]
player2_mark = get_player2_mark(player1_mark_int)

print('play now? y = yes, n = no.')
play_round = input()

while play_round.lower() == 'y':

    win = False
    counter = 9

    while not win and counter > 0:

        show_board()
        print(f'{p1_name}, select a spot')
        p1_spot = int(input())
        update_board(p1_spot, -1)
        win = check_win()

        if win:
            show_board(p1_name, win)
            break

        counter -= 1
        if counter == 0:
            show_board()
            print('tie game!  nobody wins.')
            break

        show_board()
        print(f'{p2_name}, select a spot')
        p2_spot = int(input())
        update_board(-1,p2_spot)
        win = check_win()

        if win:
            show_board(p2_name,win)
            break

        counter -= 1
    print('would you like to play again? y = yes, n = no')
    play_round = input()
    loc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('thanks for playing.  goodbye.')
