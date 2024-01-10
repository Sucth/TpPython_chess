import json
import random

class Player:
    def __init__(self, name, firstname, birthdate):
        self.Id = self.generate_unique_id()
        self.Name = self.unique_name(name)
        self.Firstname = firstname
        self.Date = birthdate
        self.Elo = 1200

    def save_info(self, players):
        players.append({"Id": self.Id, "Name": self.Name, "Firstname": self.Firstname, "Date": self.Date, "Elo": self.Elo})
        with open("joueurs.json", 'w') as f:
            json.dump(players, f, indent=4)

    def __str__(self):
        return f"Id: {self.Id}, Name: {self.Name}, Firstname: {self.Firstname}, Date: {self.Date}, Elo: {self.Elo}"
    
    def to_dict(self):
        return {
            "Id": self.Id,
            "Name": self.Name,
            "Firstname": self.Firstname,
            "Date": self.Date,
            "Elo": self.Elo
        }
    
    def generate_unique_id(self):
        players = Player.load_players()
        unique_id = None
        while not unique_id or any(player["Id"] == unique_id for player in players):
            unique_id = str(random.randint(1000, 9999))
        return unique_id
    
    def unique_name(self, player_name):
        players = Player.load_players()

        if any(player["Name"] == player_name for player in players):
            unique_name = None
            while not unique_name or any(player["Name"] == unique_name for player in players):
                unique_name = "Name#" + str(random.randint(1000, 9999))
            return unique_name
        return player_name


    @classmethod
    def delete_player_by_name(cls, player_name):
        players = cls.load_players()
        found = False

        for player in players:
            if player["Name"] == player_name:
                players.remove(player)
                found = True

        if found:
            cls.save_players(players)
            print("Player deleted successfully.")
        else:
            print("Player not found.")


    def display_players_by_name_elo(self):
        sorted_players = sorted(self.players_list, key=lambda x: (x['Name'], x['Elo']))
        for player in sorted_players:
            print(f"Name: {player['Name']}, Elo: {player['Elo']}")

    @classmethod
    def display_all_players(cls):
        players = cls.load_players()
        if players:
            print("All Players:")
            for player in players:
                print(f"ID: {player['Id']}, Name: {player['Name']}, Firstname: {player['Firstname']}, Date: {player['Date']}, Elo: {player['Elo']}")
        else:
            print("No players found.")


    def load_players():
        try:
            with open("joueurs.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_players(players):
        with open("joueurs.json", 'w') as f:
            json.dump(players, f, indent=4)

    def player_exists(cls, player_id):
        players = cls.load_players()
        for player in players:
            if player["Id"] == player_id:
                return True
        return False

    def player_exists_by_name(cls, player_name):
        players = cls.load_players()
        for player in players:
            if player["Name"] == player_name:
                return True
        return False

    def get_player_by_id(cls, player_id):
        players = cls.load_players()
        for player in players:
            if player["Id"] == player_id:
                return cls(**player)
        return

    @classmethod
    def update_player_info_by_name(cls, player_name, new_name=None, new_firstname=None, new_date=None):
        players = cls.load_players()
        found = False

        for player in players:
            if player["Name"] == player_name:
                if new_name is not None:
                    player["Name"] = new_name
                if new_firstname is not None:
                    player["Firstname"] = new_firstname
                if new_date is not None:
                    player["Date"] = new_date
                found = True

        if found:
            cls.save_players(players)
            print("Player information updated successfully.")
        else:
            print("Player not found or no changes made.")

