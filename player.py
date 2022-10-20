
gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
human = "Human"
ai = "AI"
class Player:
    
    def __init__(self, player_type=human):
        self.type = player_type
        self.name = ""
        self.gesture = self.get_gesture()

    def get_gesture(self):
        if self.type == human:
            gesture = int(input("Pick a gesture: 0 - 5"))
            print(gesture_list[gesture])
            return gesture_list[gesture]

        
    
    # def set_player_type(self, game_type):
    #     if game_type == 1:
    #         player_one = Player(player_type="human")
    #         player_two = Player()
    #     elif game_type == 2:
    #         player_one = Player(player_type="human")
    #         player_two = Player(player_type="human")
    #     else:
    #         player_one = Player()
    #         player_two = Player()
