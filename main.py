# Step 1: Display Welcome message and the rules of the game
# Step 2: Ask how many human players will be playing
# Step 3: Display list of gestures and ask for gesture input
# Step 4: display what gestures were picked by human or AI player
# Step 5: Based on rules of the game Display who won or if it is a tie 
# Step 6: Repeat process for additional rounds until there is a best-of-3 winner
from game_settings import game_settings
from game import Game


gestures = ["Rock","Paper","Scissors","Lizard","Spock"]

def welcome():
    print("Welcome to Rock Paper Scissors Lizard Spock.\n")
    print("Each match will be best of three games")
    print("Use the number keys to enter your selection\n")
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")

def main():
    welcome()
    new_game = Game(game_settings())
    print(new_game.game_type)
    print(gestures)

if __name__ == "__main__":
    main()