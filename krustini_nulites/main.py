import random
from logic import to_input
from logic import print_game_field as print_field



def noughts_crosses(who_starts):
    field = [["","","",],
             ["","","",],
             ["","","",]]
    
    while True:
        if who_starts == "O":
            field = to_input(field, "O")
            try:
                if field != "draw":
                    print_field(field)
                elif field == "draw":
                    print("It's a draw")
                    break
                    
            except:
                if field == True:
                    print("O wins")
                    break
                elif field == "draw":
                    print("It's a draw")
                    break

            field = to_input(field, "X")
            try:
                if field != "draw":
                    print_field(field)
                elif field == "draw":
                    print("It's a draw")
                    break
            except:
                if field == True:
                    print("X wins")
                    break
                elif field == "draw":
                    print("It's a draw")
                    break

# row_select = input("please select the row where you want to input")
# column_select = input("please select the column where you want to input")
if __name__ == "__main__":
    who_starts = random.choice(["X", "O"])
    print(f'{who_starts} begins the game!')
    noughts_crosses(who_starts)
