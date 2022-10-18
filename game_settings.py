
import re


def game_settings():
    num_players = input("\nHow many players? (1) Human vs AI,\n(2) Human vs Human, (3) AI vs AI: ").strip()
    while num_players not in ["1","2","3"]:
        num_players = input("\nEnter (1) Human vs AI,\n(2) Human vs Human, or (3) AI vs AI: ").strip()
    return(num_players)
