# from child_classes import rock, paper, scissors, lizard, spock
from player import Player
gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
    
class Gesture:

    def __init__(self, name:str, strong_against:tuple, weak_against:tuple):
        self.name = name
        self.strong_against = strong_against
        self.weak_against = weak_against
        pass

    def player_gesture(self, p:Player):
        pass

    