players = [{"name": "Player 1", "symbol": "X", "score": 0}, {"name": "Player 2", "symbol": "O", "score": 0}]
first_player = players[0]
second_player = players[1]
data = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
turns = 0


def print_board():
    board = (f"\n {data[0]} | {data[1]} | {data[2]} \n"
             "---+---+---\n"
             f" {data[3]} | {data[4]} | {data[5]} \n"
             "---+---+---\n"
             f" {data[6]} | {data[7]} | {data[8]} \n")
    print(board)


def check_move(player):
    global turns
    move = False
    print(f"{player['name']}'s turn!")
    while not move:
        try:
            pos = int(input("Choose a position between 1-9: "))
            if (0 < pos < 10) and data[pos - 1] == " ":
                data[pos - 1] = player["symbol"]
                turns += 1
                break
            else:
                move = False
                print("Invalid move!")
        except ValueError:
            move = False
            print("Only numbers are allowed!")


def check_winner(player):
    if (data[0] == data[1] == data[2] == player["symbol"] or data[3] == data[4] == data[5] == player["symbol"] or
            data[6] == data[7] == data[8] == player["symbol"] or data[0] == data[3] == data[6] == player["symbol"] or
            data[1] == data[4] == data[7] == player["symbol"] or data[2] == data[5] == data[8] == player["symbol"] or
            data[0] == data[4] == data[8] == player["symbol"] or data[2] == data[4] == data[6] == player["symbol"]):
        print_board()
        print(f"{player['name']} wins!\n")
        player["score"] += 1
        return False
    else:
        return True

name = input("Press Y to type your name, press Enter to skip: ")
if name.upper() == 'Y':
  first_player["name"] = input("What's your name: ").title()
  second_player["name"] = input("What's the name of the another player: ").title()


def play_game():
    game_is_on = True
    while game_is_on:
        print_board()
        if turns > 8:
            game_is_on = False
            print("It's a draw!\n")
        elif turns % 2 == 0:
            check_move(first_player)
            game_is_on = check_winner(first_player)
        else:
            check_move(second_player)
            game_is_on = check_winner(second_player)
    print(f"{first_player['name']} has {first_player['score']} points.")
    print(f"{second_player['name']} has {second_player['score']} points.")


play = True
while play:
    data = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turns = 0
    play_game()
    answer = input("\nType Y to play a new game: ").upper()
    if answer != "Y":
        print("\nGood bye, have a nice day!")
        play = False
    else:
        change = first_player
        first_player = second_player
        second_player = change