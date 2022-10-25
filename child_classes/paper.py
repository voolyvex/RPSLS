from gesture import Gesture, gesture_list
# gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
class Paper(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Paper", (gesture_list[0], gesture_list[4]), (gesture_list[2], gesture_list[3]))