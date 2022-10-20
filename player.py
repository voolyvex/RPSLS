
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
