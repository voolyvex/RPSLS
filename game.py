from player import Player, ai
class Game:
    def __init__(self):
        self.game_mode = self.game_settings()
        self.round = 1
        self.winner = False
        pass
       
    def run_game(self):
        if self.round > 3:
            self.winner = True
        else:
            print(f"Round {self.round}")
            Player.get_players(self.game_mode)
            self.fight_logic()
            self.round += 1
        pass

    def game_settings(self):
        game_mode = int(input("\nChoose game mode (1) Human vs AI,\n(2) Human vs Human, (3) AI vs AI: ").strip())
        while game_mode not in [1, 2, 3]:
            game_mode = int(input("\nEnter (1) Human vs AI,\n(2) Human vs Human, or (3) AI vs AI: ").strip())
        return game_mode
        
    def fight_logic(self):
        pass