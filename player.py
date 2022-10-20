from random import choice
from gesture import gesture_list

human = "Human"
ai = "AI"

class Player:
    
    def __init__(self, player_type:str):
        self.type = player_type
        
        self.gesture = self.get_gesture()
        pass

    def get_gesture(self):
        if self.type == human:
            gesture = int(input("Pick a gesture: 0 - 5"))
            print(gesture_list[gesture])
            return gesture_list[gesture]
        else:
            print("player is an AI")
            gesture = choice(gesture_list)
        pass

    @classmethod
    def get_players(cls, game_mode):
        if game_mode == 1:
            cls.player_one = Player(human)
            cls.player_two = Player(ai)
        elif game_mode == 2:
            cls.player_one = Player(human)
            cls.player_two = Player(human)
        else:
            cls.player_one = Player(ai)
            cls.player_two = Player(ai)
        pass
    
