from random import choice

class Player:
    gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]

    def __init__(self, player_type:str):
        self.type = player_type
        self.win_count = 0
        
    def get_gesture(self):
        if self.type == "Human":
            pick_gesture = input("Choose (1) for Rock.\nChoose (2) for Paper.\nChoose (3) for Scissors.\nChoose (4) for Lizard.\nChoose (5) for Spock.\nChoose your gesture: ").strip()
            while pick_gesture not in ["1","2","3","4","5"]:
                pick_gesture = input("Choose your gesture. (1) (2) (3) (4) or (5): ").strip()
            pick = self.gesture_list[int(pick_gesture) - 1]
        else:
            pick = choice(self.gesture_list)
        return pick    
    
