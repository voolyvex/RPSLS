from player import Player
from gesture import *
from slow_print import slow_print2
class Game:
    def __init__(self):
        self.game_mode = self.get_game_mode()
        self.round = 1
        self.winner = False
            
    def welcome(self):
        slow_print2("\nWelcome to Rock Paper Scissors Lizard Spock!  ")
        slow_print2("Each match will be best of three games.\n")
        slow_print2("Humans use the number keys to enter a selection.\n")
        slow_print2("Rock crushes Scissors..........Scissors cuts Paper\n")
        slow_print2("Paper covers Rock..............Rock crushes Lizard\n")
        slow_print2("Lizard poisons Spock...........Spock smashes Scissors\n")
        slow_print2("Scissors decapitates Lizard....Lizard eats Paper\n")
        slow_print2("Paper disproves Spock..........Spock vaporizes Rock\n")

    def get_game_mode(self):
        game_mode = input("\nChoose game mode (1) Human vs AI,\n(2) Human vs Human, (3) AI vs AI: ").strip()
        while game_mode not in ["1", "2", "3"]:
            game_mode = input("\nEnter (1) Human vs AI,\n(2) Human vs Human, or (3) AI vs AI: ").strip()
        return game_mode
    
    def get_players(self, game_mode):
        human, ai = "Human", "AI"
        if game_mode == "1":
            p1 = Player(human)
            p2 = Player(ai)
        elif game_mode == "2":
            p1 = Player(human)
            p2 = Player(human)
        else:
            p1 = Player(ai)
            p2 = Player(ai)
        return p1, p2

    def start_new_round(self, p1, p2):
        print()
        slow_print2(f"Round {self.round}\nPlayer 1 {p1.type} vs Player 2 {p2.type}\nGet ready...on Three...\n")
        slow_print2("One..... Two..... ")
        slow_print2("Three!\n")

    def run(self):
        self.welcome()
        p1, p2 = self.get_players(self.game_mode)
        while not self.winner:
            self.start_new_round(p1, p2)
            self.determine_round_winner(p1, p2)
            self.round += 1
        
    def determine_round_winner(self, p1, p2):

        # instantiate gesture objects
        rock, paper, scissors, lizard, spock = Rock(), Paper(), Scissors(), Lizard(), Spock()

        # display players' chosen gestures
        slow_print2(f"{p1.type} picks {p1.active_gesture}! ")
        slow_print2(f"{p2.type} has picked {p2.active_gesture}!\n")
        
        # adjudicate winner
        if p1.active_gesture == "Rock":
            round_winner = rock.will_defeat_or_lose(p2.active_gesture)
        elif p1.active_gesture == "Paper":
            round_winner = paper.will_defeat_or_lose(p2.active_gesture)
        elif p1.active_gesture == "Scissors":
            round_winner = scissors.will_defeat_or_lose(p2.active_gesture)
        elif p1.active_gesture == "Lizard":
            round_winner = lizard.will_defeat_or_lose(p2.active_gesture)
        else: # if p1 gesture is "Spock"
            round_winner = spock.will_defeat_or_lose(p2.active_gesture)
        
        # add to a player's win_count if they won
        if round_winner == "1":
            p1.win_count += 1
        elif round_winner == "2":
            p2.win_count += 1
        elif round_winner == "tie":
            slow_print2("It was a tie.\n")

        # check if best-of-three was won
        self.check_for_winner(p1, p2)

    def check_for_winner(self, p1, p2):
        if p1.win_count == 2:
            slow_print2(f"\nPlayer 1 {p1.type} is the winner! ")
            self.winner = True
        elif p2.win_count == 2:
            slow_print2(f"\nPlayer 2 {p2.type} is the winner! ")
            self.winner = True
        