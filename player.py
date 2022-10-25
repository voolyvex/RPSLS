
from random import choice

human = "Human"
ai = "AI"

class Player:
    
    def __init__(self, player_type:str):
        self.type = player_type
        self.gesture = ""
        self.wins = 0
        self.gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        pass

    def get_gesture(self):
        if self.type == human:
            pick_gesture = (input("Choose (0) for Rock.\nChoose (1) for Paper.\nChoose (2) for Scissors.\nChoose (3) for Lizard.\nChoose (4) for Spock.\nChoose your gesture: ")).strip()
            while pick_gesture not in ["0","1","2","3","4"]:
                pick_gesture = (input("Choose your gesture. (0) (1) (2) (3) or (4): ")).strip()
            pick = self.gesture_list[int(pick_gesture)]
        else:
            pick = choice(self.gesture_list)
        self.gesture = pick
        return self.gesture
        pass

    @classmethod
    def get_players(cls, game_mode):
        if game_mode == 1:
            return (Player(human), Player(ai))
        elif game_mode == 2:
            return (Player(human), Player(human))
        else:
            return (Player(ai), Player(ai))
        pass
    
