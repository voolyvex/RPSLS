from random import choice

gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
human = "Human"
ai = "AI"

class Player:
    
    def __init__(self, player_type):
        self.type = player_type
        self.name = ""
        self.gesture = self.get_gesture()

    def get_gesture(self):
        if self.type == human:
            gesture = int(input("Pick a gesture: 0 - 5"))
            print(gesture_list[gesture])
            return gesture_list[gesture]
        else:
            print("player is an AI")
            gesture = choice(gesture_list)

    @classmethod
    def get_players(cls, game_mode):
        if game_mode == 1:
            cls.player_one = Player(human)
            cls.player_two = Player(ai)
        elif game_mode == 2:
            player_one = Player(human)
            player_two = Player(human)
        else:
            player_one = Player(ai)
            player_two = Player(ai)
    
