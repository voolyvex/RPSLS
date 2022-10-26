#from gesture import Gesture, gesture_list
from player import Player
from child_classes import rock, paper, scissors, lizard, spock
from slow_print import slow_print, slow_print2
class Game:
    def __init__(self):
        self.game_mode = self.get_game_mode()
        self.round = 1
        self.winner = False
            
    def welcome(self, p1, p2):
        slow_print2("\nWelcome to Rock Paper Scissors Lizard Spock!  ")
        slow_print2("Each match will be best of three games.\n")
        slow_print2("Humans use the number keys to enter a selection.\n")
        slow_print2("Rock crushes Scissors..........Scissors cuts Paper\n")
        slow_print2("Paper covers Rock..............Rock crushes Lizard\n")
        slow_print2("Lizard poisons Spock...........Spock smashes Scissors\n")
        slow_print2("Scissors decapitates Lizard....Lizard eats Paper\n")
        slow_print2("Paper disproves Spock..........Spock vaporizes Rock\n")
        slow_print2(f"Player 1 {p1.type} vs Player 2 {p2.type}\n")

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

    def start_new_round(self):
        print()
        slow_print2(f"Round {self.round} get ready, on Three...\n")
        slow_print2("One....... Two....... ")
        slow_print2("Three!\n")

    def run(self):
        p1, p2 = self.get_players(self.game_mode)
        self.welcome(p1, p2)
        while not self.winner:
            self.start_new_round()
            self.determine_round_winner(p1, p2)
            self.round += 1
        pass

    
    # @classmethod
    # def show(cls, p1:Player.gesture, p2:Player.gesture):
    #     cls.rock = rock.Rock("", (), ())
    #     cls.paper = paper.Paper("", (), ())
    #     cls.scissors = scissors.Scissors("", (), ())
    #     cls.lizard = lizard.Lizard("", (), ())
    #     cls.spock = spock.Spock("", (), ())
    #     cls.gesture_objects = [cls.rock, cls.paper, cls.scissors, cls.lizard, cls.spock]
    #     cls.p1_show = object
    #     cls.p2_show = object
    #     #if it is a tie
    #     if p1 == p2:
    #         result = 2
    #         print("It was a tie.")
    #     else:
    #         for i, val in enumerate(gesture_list):
    #             if p1 == val:
    #                 cls.p1_show = Gesture.cls.gesture_objects[i]
    #             elif p2 == val:
    #                 cls.p2_show = Gesture.cls.gesture_objects[i]
    #         # if p1 wins
    #         if p2 in cls.p1_show:
    #             result = 0
    #             print("Player 1 wins the round!")
    #         # if p2 wins
    #             result = 1
    #             print("Player 2 wins the round!")

    #     return result
    #     pass
        
    def determine_round_winner(self, p1, p2):
        #players reveal gestures
        slow_print2(f"{p1.type} picks {p1.active_gesture}! ")
        slow_print2(f"{p2.type} has picked {p2.active_gesture}!\n")

        #declare winner
        round_winner = 1
        if round_winner == 0:
            p1.win_count += 1
        elif round_winner == 1:
            p2.win_count += 1
        self.check_for_winner(p1, p2)

    def check_for_winner(self, p1, p2):
        if p1.win_count == 2:
            slow_print2(f"\nPlayer 1 {p1.type} is the winner! ")
            self.winner = True
        elif p2.win_count == 2:
            slow_print2(f"\nPlayer 2 {p2.type} is the winner! ")
            self.winner = True
        pass