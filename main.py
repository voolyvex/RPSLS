# Step 1: Display Welcome message and the rules of the game
# Step 2: Ask how many human players will be playing
# Step 3: Display list of gestures and ask for gesture input
# Step 4: display what gestures were picked by human or AI player
# Step 5: Based on rules of the game Display who won or if it is a tie 
# Step 6: Repeat process for additional rounds until there is a best-of-3 winner
from game import Game
from slow_print import slow_print


def main():
    new_game = Game()
    # while new_game.winner == False:
    new_game.run()
    
    slow_print("The game has ended!\n")
    
if __name__ == "__main__":
    main()