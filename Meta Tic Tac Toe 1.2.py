#THE BOARD:
board = {"A1":" ", "A2":" ", "A3":" ", 
         "A4":" ", "A5":" ", "A6":" ",
         "A7":" ", "A8":" ", "A9":" ",
         "B1":" ", "B2":" ", "B3":" ",
         "B4":" ", "B5":" ", "B6":" ",
         "B7":" ", "B8":" ", "B9":" ",
         "C1":" ", "C2":" ", "C3":" ",
         "C4":" ", "C5":" ", "C6":" ",
         "C7":" ", "C8":" ", "C9":" ",
         "D1":" ", "D2":" ", "D3":" ",
         "D4":" ", "D5":" ", "D6":" ",
         "D7":" ", "D8":" ", "D9":" ",
         "E1":" ", "E2":" ", "E3":" ",
         "E4":" ", "E5":" ", "E6":" ",
         "E7":" ", "E8":" ", "E9":" ",
         "F1":" ", "F2":" ", "F3":" ",
         "F4":" ", "F5":" ", "F6":" ",
         "F7":" ", "F8":" ", "F9":" ",
         "G1":" ", "G2":" ", "G3":" ",
         "G4":" ", "G5":" ", "G6":" ",
         "G7":" ", "G8":" ", "G9":" ",
         "H1":" ", "H2":" ", "H3":" ",
         "H4":" ", "H5":" ", "H6":" ",
         "H7":" ", "H8":" ", "H9":" ",
         "I1":" ", "I2":" ", "I3":" ",
         "I4":" ", "I5":" ", "I6":" ",
         "I7":" ", "I8":" ", "I9":" ",
         }

def print_board():
    row1 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["A1"], board["A2"], board["A3"], board["B1"], board["B2"], board["B3"], board["C1"], board["C2"], board["C3"])
    row2 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["A4"], board["A5"], board["A6"], board["B4"], board["B5"], board["B6"], board["C4"], board["C5"], board["C6"])
    row3 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["A7"], board["A8"], board["A9"], board["B7"], board["B8"], board["B9"], board["C7"], board["C8"], board["C9"])
    row4 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["D1"], board["D2"], board["D3"], board["E1"], board["E2"], board["E3"], board["F1"], board["F2"], board["F3"])
    row5 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["D4"], board["D5"], board["D6"], board["E4"], board["E5"], board["E6"], board["F4"], board["F5"], board["F6"])
    row6 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["D7"], board["D8"], board["D9"], board["E7"], board["E8"], board["E9"], board["F7"], board["F8"], board["F9"])
    row7 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["G1"], board["G2"], board["G3"], board["H1"], board["H2"], board["H3"], board["I1"], board["I2"], board["I3"])
    row8 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["G4"], board["G5"], board["G6"], board["H4"], board["H5"], board["H6"], board["I4"], board["I5"], board["I6"])
    row9 = "| {} | {} | {} |  #  | {} | {} | {} |  #  | {} | {} | {} |" \
           .format(board["G7"], board["G8"], board["G9"], board["H7"], board["H8"], board["H9"], board["I7"], board["I8"], board["I9"])

    print()
    print(row1)
    print(row2)
    print(row3)
    for i in range(1,26):
        print("#", end=' ')
    print()
    print(row4)
    print(row5)
    print(row6)
    for i in range(1,26):
        print("#", end=' ')
    print()
    print(row7)
    print(row8)
    print(row9)
    print()

meta_board = {
    "A":" ", "B":" ", "C":" ", 
    "D":" ", "E":" ", "F":" ",
    "G":" ", "H":" ", "I":" "}


#OTHER TOOLS
zones = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
first_play = 0


#ZONE RESTRICTION
gchoice = "z"
current_zone = "A-I"

#GAMEPLAY START
print("* * * WELCOME to META TIC TAC TOE * * *")
while True:
    p1icon = input("Player 1, what would you like your icon to be?: ").strip()
    if len(p1icon) > 1:
        print("Limit your icon to one character.")
    else:
        break

while True:
    p2icon = input("Player 2, what would you like your icon to be?: ").strip()
    if len(p2icon) > 1:
        print("Limit your icon to one character.")
    elif p2icon == p1icon:
        print("Sorry, you cannot choose the same icon as Player 1.")
    else:
        break

print("Player 1 starts.")


#DEFINITIONS
def initial():
    global first_play
    first_play = first_play + 1

def zone_restriction():
    global gchoice
    global current_zone
    if "z" in gchoice:
        current_zone = "A-I"
    if "1" in gchoice:
        current_zone = "A"
    if "2" in gchoice:
        current_zone = "B"
    if "3" in gchoice:
        current_zone = "C"
    if "4" in gchoice:
        current_zone = "D"
    if "5" in gchoice:
        current_zone = "E"
    if "6" in gchoice:
        current_zone = "F"
    if "7" in gchoice:
        current_zone = "G"
    if "8" in gchoice:
        current_zone = "H"
    if "9" in gchoice:
        current_zone = "I"

def first_move():
    global first_play
    if first_play == 0:
        print_board()
        global current_zone
        input_zone = current_zone
        print("Your turn Player 1.")
        choice = input("Enter your move (Zone {}): ".format(input_zone)).strip()
        global gchoice
        gchoice = choice
        try:
            if board[choice] == " " and choice in board:
                board[choice] = p1icon
            elif board[choice] == " " and choice not in board:
                print("Invalid space. Please make a move A1-I9.".format(input_zone))
                first_move()
        except KeyError:
            print("Invalid move.")
            first_move()

def player2_move(p2icon):
    global current_zone
    input_zone = current_zone
    print("Your turn Player 2.")
    choice = input("Enter your move (Zone {}): ".format(input_zone)).strip()
    global gchoice
    gchoice = choice
    try:
        if board[choice] == " " and input_zone in choice:
            board[choice] = p2icon
        elif board[choice] == " " and input_zone not in choice:
            print("Incorrect zone. Play in Zone {}.".format(input_zone))
            player2_move(p2icon)
        elif board[choice] != " ":
            print("That space is taken, fool!")
            player2_move(p2icon)
    except KeyError:
        print("Invalid move.")
        player2_move(p2icon)

def player1_move(p1icon):
    global current_zone
    input_zone = current_zone
    print("Your turn Player 1.")
    choice = input("Enter your move (Zone {}): ".format(input_zone)).strip()
    global gchoice
    gchoice = choice
    try:
        if board[choice] == " " and input_zone in choice:
            board[choice] = p1icon
        elif board[choice] == " " and input_zone not in choice:
            print("Incorrect zone. Play in Zone {}.".format(input_zone))
            player1_move(p1icon)
        elif board[choice] != " ":
            print("That space is taken, fool!")
            player1_move(p1icon)
    except KeyError:
            print("Invalid move.")
            player1_move(p1icon)

def zone_victory1(p1icon):
    for letters in zones:
        if board["{}1".format(letters)]==p1icon and board["{}2".format(letters)]==p1icon and board["{}3".format(letters)]==p1icon or \
           board["{}4".format(letters)]==p1icon and board["{}5".format(letters)]==p1icon and board["{}6".format(letters)]==p1icon or \
           board["{}7".format(letters)]==p1icon and board["{}8".format(letters)]==p1icon and board["{}9".format(letters)]==p1icon or \
           board["{}1".format(letters)]==p1icon and board["{}4".format(letters)]==p1icon and board["{}7".format(letters)]==p1icon or \
           board["{}2".format(letters)]==p1icon and board["{}5".format(letters)]==p1icon and board["{}8".format(letters)]==p1icon or \
           board["{}3".format(letters)]==p1icon and board["{}6".format(letters)]==p1icon and board["{}9".format(letters)]==p1icon or \
           board["{}1".format(letters)]==p1icon and board["{}5".format(letters)]==p1icon and board["{}9".format(letters)]==p1icon or \
           board["{}3".format(letters)]==p1icon and board["{}5".format(letters)]==p1icon and board["{}3".format(letters)]==p1icon:
            for num in numbers:
                board["{}{}".format(letters, num)] = p1icon
            print("Player 1 wins Zone {}.".format(letters))
            global meta_board
            meta_board["{}".format(letters)] = p1icon
            zones.remove(letters)

def zone_victory2(p2icon):
    for letters in zones:
        if board["{}1".format(letters)]==p2icon and board["{}2".format(letters)]==p2icon and board["{}3".format(letters)]==p2icon or \
           board["{}4".format(letters)]==p2icon and board["{}5".format(letters)]==p2icon and board["{}6".format(letters)]==p2icon or \
           board["{}7".format(letters)]==p2icon and board["{}8".format(letters)]==p2icon and board["{}9".format(letters)]==p2icon or \
           board["{}1".format(letters)]==p2icon and board["{}4".format(letters)]==p2icon and board["{}7".format(letters)]==p2icon or \
           board["{}2".format(letters)]==p2icon and board["{}5".format(letters)]==p2icon and board["{}8".format(letters)]==p2icon or \
           board["{}3".format(letters)]==p2icon and board["{}6".format(letters)]==p2icon and board["{}9".format(letters)]==p2icon or \
           board["{}1".format(letters)]==p2icon and board["{}5".format(letters)]==p2icon and board["{}9".format(letters)]==p2icon or \
           board["{}3".format(letters)]==p2icon and board["{}5".format(letters)]==p2icon and board["{}3".format(letters)]==p2icon:
            for num in numbers:
                board["{}{}".format(letters, num)] = p2icon
            print("Player 2 wins Zone {}.".format(letters))
            global meta_board
            meta_board["{}".format(letters)] = p2icon
            zones.remove(letters)

def total_victory1(p1icon):
    if meta_board["A"]==p1icon and meta_board["B"]==p1icon and meta_board["C"]==p1icon or \
       meta_board["D"]==p1icon and meta_board["E"]==p1icon and meta_board["F"]==p1icon or \
       meta_board["G"]==p1icon and meta_board["H"]==p1icon and meta_board["I"]==p1icon or \
       meta_board["A"]==p1icon and meta_board["D"]==p1icon and meta_board["G"]==p1icon or \
       meta_board["B"]==p1icon and meta_board["E"]==p1icon and meta_board["H"]==p1icon or \
       meta_board["C"]==p1icon and meta_board["F"]==p1icon and meta_board["I"]==p1icon or \
       meta_board["A"]==p1icon and meta_board["E"]==p1icon and meta_board["I"]==p1icon or \
       meta_board["C"]==p1icon and meta_board["E"]==p1icon and meta_board["G"]==p1icon:
            return True
    else:
        return False

def total_victory2(p2icon):
    if meta_board["A"]==p2icon and meta_board["B"]==p2icon and meta_board["C"]==p2icon or \
       meta_board["D"]==p2icon and meta_board["E"]==p2icon and meta_board["F"]==p2icon or \
       meta_board["G"]==p2icon and meta_board["H"]==p2icon and meta_board["I"]==p2icon or \
       meta_board["A"]==p2icon and meta_board["D"]==p2icon and meta_board["G"]==p2icon or \
       meta_board["B"]==p2icon and meta_board["E"]==p2icon and meta_board["H"]==p2icon or \
       meta_board["C"]==p2icon and meta_board["F"]==p2icon and meta_board["I"]==p2icon or \
       meta_board["A"]==p2icon and meta_board["E"]==p2icon and meta_board["I"]==p2icon or \
       meta_board["C"]==p2icon and meta_board["E"]==p2icon and meta_board["G"]==p2icon:
        return True
    else:
        return False

#GAMEPLAY LOOP
while True:
    first_move()
    zone_restriction()
    zone_victory1(p1icon)
    if total_victory1(p1icon):
        print("Player 1 wins the game.")
        print_board()
        print("* * * GAME OVER * * *")
        break

    print_board()
    player2_move(p2icon)
    zone_restriction()
    zone_victory2(p2icon)
    if total_victory2(p2icon):
        print("Player 2 wins the game.")
        print_board()
        print("* * * GAME OVER * * *")
        break
    print_board()
    
    initial()
    
    player1_move(p1icon)
    zone_restriction()
    zone_victory1(p1icon)
    if total_victory1(p1icon):
        print("Player 1 wins the game.")
        print_board()
        print("* * * GAME OVER * * *")
        break
    
