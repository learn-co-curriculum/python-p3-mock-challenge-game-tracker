class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise AttributeError(
                "Username must be a string between 2 and 16 characters included."
            )

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise AttributeError("Player must be an instance of class Player")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise AttributeError("Game must be an instance of class Game")


from classes.player import Player
from classes.game import Game