import json
import random
import Tournois
import Matchs
from Player import Player

class Terminal:
    def __init__(self):
        self.players_list = self.load_players()
        self.current_tournament = None

    def run(self):
        while True:
            print("========Chess========")
            print("1. Add Player                       ->    Ajouter un nouveau Joueur")
            print("2. Update Player                    ->    Modifier un Joueur")
            print("3. Display Player                   ->    Afficher tous les Joueurs")
            print("4. Delete Player                    ->    Supprimer Un Joueur")
            print("5. Create Tournament                ->    Cree un Tournois")
            print("6. Display Tournament               ->    Afficher tous les Tournois")
            print("7. Add Player Tournament            ->    ")
            print("8. create all  Match Tournament     ->    A faire une fois tous les joueurs ajouter")
            print("9. Start match                      ->    ")
            print("9. Quit                             ->    Quitter le programme")

            user_input = input("Enter your choice: ")
            if user_input == "1":
                self.add_player()
            elif user_input == "2":
                self.update_player()
            elif user_input == "3":
                Player.display_all_players()
            elif user_input == "4":
                self.delete_player()
            elif user_input == "5":
                self.create_tournois()
            elif user_input == "6":
                self.display_all_tournaments()
            elif user_input == "7":
                self.add_player_at_tournament()
            elif user_input == "8":
                self.add_match()
            elif user_input == "9":
                self.start_match()


            elif user_input == "" or user_input.lower() == "quit":
                print("Exiting program.")
                self.save_players()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def start_match(self):
        new_match = Matchs.Match("w", "w", None)
        new_match.play_all_matches()

    def add_match(self):
        new_tournament = Tournois.Tournament("Nom du Tournoi", "2024-01-09")
        name_tournois = str(input("Enter Tournament name: "))

        new_tournament.create_all_vs_all_matches(name_tournois)

    def add_player_at_tournament(self):
        if self.current_tournament:
            name_player = input("Enter player name: ")
            self.current_tournament.add_player(name_player)
            print(f"{name_player} added to the tournament.")
        else:
            print("No tournament selected. Please create a tournament first.")


    def create_tournois(self):
        name = input("Enter Tournament name: ")
        date = input("Enter tournament date: ")

        new_tournament = Tournois.Tournament(name, date)
        new_tournament.create_tournament(name, date)

        self.current_tournament = new_tournament


    def display_all_tournaments(self):
        Tournois.Tournament.display_all_tournaments()
        
    def load_players(self):
        try:
            with open("joueurs.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_players(self):
        with open("joueurs.json", 'w') as f:
            json.dump(self.players_list, f, indent=4)

    def add_player(self):
        name = input("Enter player name: ")
        firstname = input("Enter player firstname: ")
        birthdate = input("Enter player birthdate (YYYY-MM-DD): ")

        player = Player(name, firstname, birthdate)
        self.players_list.append(player.to_dict())
        self.save_players()
        print("Player added successfully.")

    def update_player(self):
        player_name = input("Enter player name: ")
        name = input("Enter updated player name: ")
        firstname = input("Enter updated player firstname: ")
        birthdate = input("Enter updated player birthdate (YYYY-MM-DD): ")

        Player.update_player_info_by_name(player_name, name, firstname, birthdate)

    def delete_player(self):
        player_name = input("Enter player name to delete: ")
        Player.delete_player_by_name(player_name)