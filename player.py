from random import choice

class Player:
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]

    def __init__(self, player_type:str):
        self.type = player_type
        self.win_count = 0
        
    def get_gesture(self, gesture):
        if self.type == "Human":
            pick_gesture = gesture
            pick = self.gesture_list[int(pick_gesture) - 1]
        else:
            pick = choice(self.gesture_list)
        return pick    
    
