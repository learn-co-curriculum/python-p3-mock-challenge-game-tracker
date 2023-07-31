class Player:
    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise AttributeError(
                "Username must be a string between 2 and 16 characters included."
            )

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return [result.game for result in self.results()]

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return self.games_played().count(game)

    @classmethod
    def highest_scored(cls, game):
        averages = [(game.average_score(player), player) for player in cls.all]
        if not averages:
            return None
        highest_record_tuple = max(averages, key=lambda tup: tup[0])
        return highest_record_tuple[1]
    
from classes.result import Result