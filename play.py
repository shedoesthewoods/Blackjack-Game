from blackjack import game

play_game = "y"

while play_game == "y":
    play_game = input("You want to play a game? (y/n): ")
    if play_game == "y":
        game()
    elif play_game == "n":
        break
    else:
        play_game = "y"
        print("y or n?")
