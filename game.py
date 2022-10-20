from player import Player, ai
class Game:
    def __init__(self):
        self.game_mode = self.game_settings()
        self.round = 1
        self.winner = False
    
    

    def run_game(self):
        if self.round > 3:
            self.winner = True
        else:
            print(f"Round {self.round}")
            self.round += 1
            Player.get_players(self.game_mode)
            

    

    def game_settings(self):
        game_mode = int(input("\nChoose game mode (1) Human vs AI,\n(2) Human vs Human, (3) AI vs AI: ").strip())
        while game_mode not in [1, 2, 3]:
            game_mode = int(input("\nEnter (1) Human vs AI,\n(2) Human vs Human, or (3) AI vs AI: ").strip())
        return game_mode
        