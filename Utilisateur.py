import json
from Player import Player

class Terminal:
    def __init__(self):
        self.players_list = []

    def run(self):
        while True:
            print("========Chess========")
            print("1. Add Player               ->    Ajouter un nouveau Joueur")
            print("2. Quit                     ->    Quitter le programme")

            user_input = input("Enter your choice: ")

            if user_input == "1":
                self.add_player()
            elif user_input.lower() == "2" or user_input.lower() == "quit":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def add_player(self):
        player_id = int(input("Enter player ID: "))
        name = input("Enter player name: ")
        firstname = input("Enter player firstname: ")
        birthdate = input("Enter player birthdate (YYYY-MM-DD): ")
        elo = int(input("Enter player Elo: "))

        player = Player(player_id, name, firstname, birthdate, elo)
        self.players_list.append(player.to_dict())
        self.save_players()
        print("Player added successfully.")

    def save_players(self):
        with open("joueurs.json", 'w') as f:
            json.dump(self.players_list, f, indent=4)
