from player import Player
class Game:
    def __init__(self, num_players, player_one, player_two):
        self.game_type = int(num_players)
        self.player_one = Player(self.game_type)
        