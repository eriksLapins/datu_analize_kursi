def check_range(row_or_column):
    """
        Checks if the provided number is either 1, 2, or 3
            returns True if it is, and a descriptive error message if it is not.
    """
    if row_or_column in range(0,3):
        return True
    elif row_or_column > 2:
        return "Number too large"
    elif row_or_column < 0:
        return "Number too low"


def select_row(who_plays):
    """
        Selects the row in which to input O or X
    """
    while True:
        try:
            row_select = int(input(f"{who_plays} selects the row where to input (1 - 3)"))-1
        except ValueError:
            print("No number or nothing given")
            continue
        
        if check_range(row_select) == True:
            return row_select
        elif check_range(row_select):
            print(check_range(row_select))
            continue
    

def select_column(who_plays):
    """
        Selects the column in which to input O or X
    """
    while True:
        try:
            column_select = int(input(f"{who_plays} selects the column where to input (1 - 3)"))-1
        except ValueError:
            print("No number or nothing given")
            continue

        if check_range(column_select) == True:
            return column_select
        elif check_range(column_select):
            print(check_range(column_select))
            continue

def empty_print(game_field, row, column):
    if game_field[row][column] == "":
        return " "
    else:
        return game_field[row][column]
    

def print_game_field(game_field):

    print(" "  + empty_print(game_field, 0, 0) + "|" + empty_print(game_field, 0, 1) + "|" + empty_print(game_field, 0, 2))
    print("-------")
    print(" "  + empty_print(game_field, 1, 0) + "|" + empty_print(game_field, 1, 1) + "|" + empty_print(game_field, 1, 2))
    print("-------")
    print(" "  + empty_print(game_field, 2, 0) + "|" + empty_print(game_field, 2, 1) + "|" + empty_print(game_field, 2, 2))



def check_if_empty(game_field, row_select, column_select):
    """
        Checks if the input place is empty or not
    """
    where_to_input = game_field[row_select][column_select]
    if where_to_input == "":
        return True
    else:
        return False


def check_if_win(game_field, row_select, column_select, input_value):
    """
        Checks if the game should be over because someone has won
    """
    # check if the current row is full of O or X
    if game_field[row_select].count(input_value) == 3:
        return True
    
    # check if the current column is full of O ir X
    elif game_field[0][column_select] == input_value and game_field[1][column_select] == input_value and game_field[2][column_select] == input_value:
        return True
    
    # check if one of the diagonals is full of O or X
    elif game_field[0][0] == input_value and game_field[1][1] == input_value and game_field[2][2] == input_value:
        return True
    elif game_field[2][0] == input_value and game_field[1][1] == input_value and game_field[0][2] == input_value:
        return True


def check_row_multiple(game_field):
    """
        Checks if a row has O and X
    """

    r1 = False
    r2 = False
    r3 = False

    if game_field[0].count("O") >= 1 and game_field[0].count("X") >= 1:
        r1 = True
    if game_field[1].count("O") >= 1 and game_field[1].count("X") >= 1:
        r2 = True
    if game_field[2].count("O") >= 1 and game_field[2].count("X") >= 1:
        r3 = True
    
    if r1 == True and r2 == True and r3 == True:
        return True


def check_column_multiple(game_field):
    """
        Checks if a column has O and X
    """
    column_1 = [game_field[0][0], game_field[1][0], game_field[2][0]]
    column_2 = [game_field[0][1], game_field[1][1], game_field[2][1]]
    column_3 = [game_field[0][2], game_field[1][2], game_field[2][2]]

    c1 = False
    c2 = False
    c3 = False    


    if column_1.count("O") >= 1 and column_1.count("X") >= 1:
        c1 = True
    if column_2.count("O") >= 1 and column_2.count("X") >= 1:
        c2 = True
    if column_3.count("O") >= 1 and column_3.count("X") >= 1:
        c3 = True
    
    if c1 == True and c2 == True and c3 == True:
        return True
    else:
        return False
    
    
def check_diagonal_multiple(game_field):
    """
        Checks if any diagonal has O and X
    """
    diagonal_1 = [game_field[0][0], game_field[1][1], game_field[2][2]]
    diagonal_2 = [game_field[2][0], game_field[1][1], game_field[0][2]]
    
    d1 = False
    d2 = False
    
    if diagonal_1.count("O") >= 1 and diagonal_1.count("X") >= 1:
        d1 = True
    if diagonal_2.count("O") >= 1 and diagonal_2.count("X") >= 1:
        d2 = True
    
    if d1 == True and d2 == True:
        return True
    else:
        return False    


def check_field_full(game_field):
    i = 0
    for row in game_field:
        if row.count("") == 0:
            i += 1
    if i == 3:
        return True


def check_if_not_game(rows_multi, columns_multi, diagonals_multi, game_field):
    """
        Checks if the game can be finished:
            returns True if the game cannot be finished
    """
    if rows_multi == True and columns_multi == True and diagonals_multi == True:
        return True    
    if check_field_full(game_field):
        return True


def to_input(game_field, input_value):
    """
        Here we define the input row and column, and check if the game has been won
    """
    while True:
        row_select = select_row(input_value)
        column_select = select_column(input_value)
        
        where_to_input = game_field[row_select][column_select]
        
        if where_to_input == "":
            game_field[row_select][column_select] = input_value
            break
        else:
            print("Please select an another postition, this one is taken")
            continue
    

    if check_if_win(game_field, row_select, column_select, input_value) == True:
        print_game_field(game_field)
        return True


    check_row = check_row_multiple(game_field)
    check_column = check_column_multiple(game_field)
    check_diagonal = check_diagonal_multiple(game_field)
    check_not_game = check_if_not_game(check_row, check_column, check_diagonal, game_field)
    
    if check_not_game == True:
        print_game_field(game_field)
        return "draw"

    
    return game_field
    