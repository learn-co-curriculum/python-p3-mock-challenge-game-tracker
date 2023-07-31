class Game:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self, "title") and title and isinstance(title, str):
            self._title = title
        else:
            raise AttributeError(
                "Title must be a non-empty string and cannot be changed."
            )

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return [result.player for result in self.results()]

    def average_score(self, player):
        scores = [result.score for result in player.results() if result.game is self]
        return mean(scores) if len(scores) else 0


from classes.result import Result
from statistics import mean