import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n'


def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)


def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1  # (3,1)


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST
    return valid_directions


def pull_lever(col,row,coins):
    ''' Find if there is a lever on the tile and offer the option to pull it '''

    if (col == 1 and row == 2) or (col == 2 and row == 2) or (col == 2 and row == 3) or (col == 3 and row == 2):
        choice = random.choice([YES, NO])
        print('Pull a lever (y/n): {}'.format(choice))

        if choice == 'y':
            coins += 1
            print('You received 1 coin, your total is now {}.'.format(coins))
    return coins


def play_one_move(col, row, valid_directions,coins,move_counter):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice([NORTH, EAST, SOUTH, WEST])
    print("Direction: {}".format(direction))
    move_counter += 1

    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        coins = pull_lever(col, row, coins)
    return victory, col, row, coins, move_counter


my_seed = int(input('Input seed: '))
random.seed(my_seed)
keep_playing = 'y'
while keep_playing == 'y':
    # The main program starts here
    victory = False
    row = 1
    col = 1
    coins = 0
    move_counter = 0

    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, coins,move_counter = play_one_move(col, row, valid_directions,coins,move_counter)
    print("Victory! Total coins {}. Moves {}.".format(coins,move_counter))
    keep_playing = input('Play again (y/n): ').lower()
