    
class Gesture:
    def __init__(self, name:str, strong_against:tuple, weak_against:tuple):
        self.name = name
        self.strong_against = strong_against
        self.weak_against = weak_against
        pass

class Rock(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Rock", (gesture_list[2], gesture_list[3]), (gesture_list[1], gesture_list[4]))

class Paper(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Paper", (gesture_list[0], gesture_list[4]), (gesture_list[2], gesture_list[3]))
    
class Scissors(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Scissors", (gesture_list[1], gesture_list[3]), (gesture_list[0], gesture_list[4]))
    
class Lizard(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Lizard", (gesture_list[1], gesture_list[4]), (gesture_list[0], gesture_list[2]))

class Spock(Gesture):
    def __init__(self, name: str, strong_against: tuple, weak_against: tuple):
        super().__init__("Spock", (gesture_list[0], gesture_list[2]), (gesture_list[1], gesture_list[3]))