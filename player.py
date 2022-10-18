from game import Game

class Player:
    def __init__(self, player_type="AI"):
        self.type = player_type
        self.name = ""
    
    def set_player_type(self, game_type):
        if game_type == 1:
            player_one = Player(player_type="human")
            player_two = Player()
        elif game_type == 2:
            player_one = Player(player_type="human")
            player_two = Player(player_type="human")
        else:
            player_one = Player()
            player_two = Player()
