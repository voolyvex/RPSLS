
class Gesture:
    
    def __init__(self, name:str):
        self.name = name
        self.image = "img/spock.jpg"
        
    def will_defeat_or_lose(self):
        print("We are the champions, my friends.")

class Rock(Gesture):
    def __init__(self):
        super().__init__("Rock")
        self.image_left.PixMap(self.image)
        
    def will_defeat_or_lose(self, p2_gesture: str):
        if p2_gesture in ["Scissors", "Lizard"]:
            return "1"
        elif p2_gesture in ["Paper", "Spock"]:
            return "2"
        elif p2_gesture == self.name:
            return "tie"

class Paper(Gesture):
    def __init__(self):
        super().__init__("Paper")
    
    def will_defeat_or_lose(self, p2_gesture: str):
        if p2_gesture in ["Rock", "Spock"]:
            return "1"
        elif p2_gesture in ["Scissors", "Lizard"]:
            return "2"
        elif p2_gesture == self.name:
            return "tie"

class Scissors(Gesture):
    def __init__(self):
        super().__init__("Scissors")
    
    def will_defeat_or_lose(self, p2_gesture: str):
        if p2_gesture in ["Paper", "Lizard"]:
            return "1"
        elif p2_gesture in ["Rock", "Spock"]:
            return "2"
        elif p2_gesture == self.name:
            return "tie"

class Lizard(Gesture):
    def __init__(self):
        super().__init__("Lizard")
    
    def will_defeat_or_lose(self, p2_gesture: str):
        if p2_gesture in ["Paper", "Spock"]:
            return "1"
        elif p2_gesture in ["Scissors", "Rock"]:
            return "2"
        elif p2_gesture == self.name:
            return "tie"

class Spock(Gesture):
    def __init__(self):
        super().__init__("Spock")
    
    def will_defeat_or_lose(self, p2_gesture: str):
        if p2_gesture in ["Scissors", "Rock"]:
            return "1"
        elif p2_gesture in ["Paper", "Lizard"]:
            return "2"
        elif p2_gesture == self.name:
            return "tie"