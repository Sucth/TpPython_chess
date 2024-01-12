import json
from itertools import combinations
import random
import Tournois
from Player import Player

class Match:
    def __init__(self, player1, player2, result=None):
        self.player1 = player1
        self.player2 = player2
        self.result = result

    def get_winner(self):
        if self.result == "1-0":
            return self.player1
        elif self.result == "0-1":
            return self.player2
        else:
            return None

    def get_loser(self):
        if self.result == "1-0":
            return self.player2
        elif self.result == "0-1":
            return self.player1
        else:
            return None
            
    def update_player_elo(self, player1, player2, result, players_file='joueurs.json'):
        with open(players_file, 'r') as players_file:
            players_data = json.load(players_file)

        for player_data in players_data:
            if player_data["Name"] == player1:
                if result == "1-0":
                    player_data["Elo"] += 100
                elif result == "0-1":
                    player_data["Elo"] -= 100

            elif player_data["Name"] == player2:
                if result == "1-0":
                    player_data["Elo"] -= 100
                elif result == "0-1":
                    player_data["Elo"] += 100

        with open('joueurs.json', 'w') as players_file:
            json.dump(players_data, players_file, indent=4)


    def display_all_players_from_matches(self):
        with open('tournois.json', 'r') as file:
            data = json.load(file)

        all_players = set()

        for tournament in data:
            matches = tournament.get("matches", [])
            for match in matches:
                player1 = match.get("player1")
                player2 = match.get("player2")
                if player1:
                    all_players.add(player1)
                if player2:
                    all_players.add(player2)

        print("All players from matches:")
        for player in all_players:
            print(player)

    @staticmethod
    def play_all_matches(self):
        with open('tournois.json', 'r') as file:
            data = json.load(file)

        for tournament in data:
            matches = tournament.get("matches", [])
            for match in matches:
                player1 = match.get("player1")
                player2 = match.get("player2")
                
                if player1 and player2:
                    result = self.simulate_match()
                    new_match = Match(player1, player2, result)
                    new_match.display_match_result(player1, player2, result)
                    self.update_player_elo(player1, player2, result)

    def simulate_match(self):
        result = random.choice(["1-0", "0-1", "0.5-0.5"])
        return result


    def display_match_result(self, player1, player2, result):
        print(f"{player1} VS {player2} = {result}")
        Tournois.Tournament.display_match_result(self, player1, player2, result)
