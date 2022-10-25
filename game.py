#from gesture import Gesture, gesture_list
from player import *
from child_classes import rock, paper, scissors, lizard, spock
from slow_print import slow_print
class Game:
    def __init__(self):
        self.game_mode = self.get_game_mode()
        self.round = 1
        self.winner = False
        self.player_one = None
        self.player_two = None
        self.player_tup = (self.player_one, self.player_two)
        self.player_tup = Player.get_players(self.game_mode)

        # self.rock = object
        # self.paper = object
        # self.scissors = object
        # self.lizard = object
        # self.spock = object

        # self.p1_show = object
        # self.p2_show = object
        pass
    
    def welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.\n")
        print("Each match will be best of three games.")
        print("Use the number keys to enter your selection.\n")
        print("Rock crushes Scissors.")
        print("Scissors cuts Paper.")
        print("Paper covers Rock.")
        print("Rock crushes Lizard.")
        print("Lizard poisons Spock.")
        print("Spock smashes Scissors.")
        print("Scissors decapitates Lizard.")
        print("Lizard eats Paper.")
        print("Paper disproves Spock.")
        print("Spock vaporizes Rock.")

    def run(self):
        self.welcome()
        while self.winner == False:
            print(f"Round {self.round} get ready, on Three...")
            slow_print("One... Two....")
            slow_print(".....")
            print("Three!\n")
            self.fight_logic()
            
            self.round += 1
        pass

    def get_game_mode(self):
        game_mode = input("\nChoose game mode (1) Human vs AI,\n(2) Human vs Human, (3) AI vs AI: ").strip()
        while game_mode not in ["1", "2", "3"]:
            game_mode = input("\nEnter (1) Human vs AI,\n(2) Human vs Human, or (3) AI vs AI: ").strip()
        return game_mode
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
        
    def fight_logic(self, round_winner = 0):
        print(f"{self.player_one.type} picks {self.player_one.get_gesture}.")
        print(f"{self.player_two.type} has picked {self.player_two.get_gesture}.")
        round_winner = 1
        if round_winner == 0:
            Player.player_one.wins += 1
        elif round_winner == 1:
            Player.player_two.wins += 1
        self.win_logic()

    def win_logic(self):
        if Player.player_one.wins == 2:
            slow_print("Player One is the winner.")
            self.winner = True
        elif Player.player_two.wins == 2:
            slow_print("Player Two is the winner.")
            self.winner = True
        pass