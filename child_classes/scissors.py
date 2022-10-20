from gesture import Gesture, gesture_list
# gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
class Scissors(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Scissors", (gesture_list[1], gesture_list[3]), (gesture_list[0], gesture_list[5]))