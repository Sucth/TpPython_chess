class Tournament:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.players = []
        self.matches = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_match(self, match):
        self.matches.append(match)

    def remove_match(self, match):
        self.matches.remove(match)