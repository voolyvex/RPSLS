from gesture import Gesture
# gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
class Spock(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__(name, strong_against, weak_against)