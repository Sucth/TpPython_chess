import json
from Player import Player
import Matchs
from itertools import combinations
import csv

class Tournament:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.players = []
        self.matches = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            print(f"{player} n'est pas dans la liste des joueurs.")

    def add_match(self, match):
        self.matches.append(match)

    def remove_match(self, match):
        if match in self.matches:
            self.matches.remove(match)
        else:
            print("Ce match n'existe pas dans la liste.")

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "players": self.players,
            "matches": self.matches
        }

    @staticmethod
    def create_tournament(name, date):
        tournament = Tournament(name, date)
        try:
            with open('tournois.json', 'r+') as file:
                data = json.load(file)
                data.append(tournament.to_dict())
                file.seek(0)
                json.dump(data, file, indent=4)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open('tournois.json', 'w') as file:
                json.dump([tournament.to_dict()], file, indent=4)

    @staticmethod
    def update_tournament(tournament_name, new_date):
        with open('tournois.json', 'r+') as file:
            data = json.load(file)
            for tournament in data:
                if tournament['name'] == tournament_name:
                    tournament['date'] = new_date
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    break
            else:
                print("Tournoi non trouvé.")

    @staticmethod
    def delete_tournament(tournament_name):
        with open('tournois.json', 'r+') as file:
            data = json.load(file)
            for tournament in data:
                if tournament['name'] == tournament_name:
                    data.remove(tournament)
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    break
            else:
                print("Tournoi non trouvé.")

    @staticmethod
    def load_tournaments():
        try:
            with open('tournois.json', 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Fichier de tournois introuvable.")
            return []

    def create_all_vs_all_matches(self, tournament_name):
        with open('tournois.json', 'r') as file:
            data = json.load(file)

        for tournament in data:
            if tournament.get("name") == tournament_name:
                players = tournament.get("players", [])
                if players:
                    all_matches = []
                    for player1, player2 in combinations(players, 2):
                        match = {"player1": player1, "player2": player2}
                        all_matches.append(match)
                    tournament["matches"] = all_matches

        with open('tournois.json', 'w') as file:
            json.dump(data, file, indent=4)


    @staticmethod
    def save_tournaments(tournaments):
        with open('tournois.json', 'w') as file:
            json.dump(tournaments, file, indent=4)

    def add_players_to_tournament(self, tournament_name, player_names):
        tournament_data = Tournament.load_tournaments()
        players = Player.load_players()

        if isinstance(player_names, str):
            player_names = [player_names]

        players_to_add = []
        for name in player_names:
            if Player.player_exists_by_name(Player, name):
                players_to_add.append(name)
            else:
                print(f"Player {name} does not exist.")

        for tournament in tournament_data:
            if tournament['name'] == tournament_name:
                for player_name in players_to_add:
                    tournament['players'].append(player_name)
                Tournament.save_tournaments(tournament_data)
                print(f"{len(players_to_add)} players added to tournament {tournament_name}.")
                return
        print("Tournament not found.")

    def add_match(self, tournament_name, player1, player2):
        tournament_data = Tournament.load_tournaments()

        for tournament in tournament_data:
            if tournament['name'] == tournament_name:
                players_in_tournament = tournament['players']
                if player1 in players_in_tournament and player2 in players_in_tournament:
                    match = {"player1": player1, "player2": player2}
                    tournament['matches'].append(match)
                    Tournament.save_tournaments(tournament_data)
                    print(f"{player1} vs {player2} added to tournament {tournament_name}.")
                    return
                else:
                    print(f"One or both players are not in the tournament.")
                    return

        print("Tournament not found.")

    @staticmethod
    def display_all_tournaments():
        tournaments = Tournament.load_tournaments()
        if tournaments:
            print("All Tournaments:")
            for tournament in tournaments:
                print(f"Name: {tournament['name']}, Date: {tournament['date']}")
                if tournament['players']:
                    print("Players:")
                    for player in tournament['players']:
                        print(f" - {player}")
                else:
                    print("No players in this tournament.")
                    
                if tournament['matches']:
                    print("Matches:")
                    for match in tournament['matches']:
                        print(f" - {match['player1']} vs {match['player2']}")
                else:
                    print("No matches in this tournament.")
                print()
        else:
            print("No tournaments found.")

    def display_match_result(self, player1, player2, result):
        print(f"{player1} VS {player2} = {result}")

        tournament_csv_file = f"result_{self.name}.csv"
        with open(tournament_csv_file, mode='a', newline='') as csvfile:
            fieldnames = ['Player1', 'Player2', 'Result']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'Player1': player1, 'Player2': player2, 'Result': result})

    def display_players_and_matches(self):
        if self.players:
            print("Players:")
            for player in self.players:
                print(f" - {player}")
        else:
            print("No players in this tournament.")

        if self.matches:
            print("Matches:")
            for match in self.matches:
                print(f" - {match['player1']} vs {match['player2']}")
        else:
            print("No matches in this tournament.")
