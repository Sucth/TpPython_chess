import json
class Player:

    def __init__(self, Id, Name, Firstname, Date, Elo):
        self.Id = Id
        self.Name = Name
        self.Firstname = Firstname
        self.Date = Date
        self.Elo = Elo

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