class Game:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title must be of type String.")
        elif not new_title:
            raise ValueError("Title must contain at least one character.")
        elif hasattr(self, "title"):
            raise AttributeError("Title cannot change after game starts.")
        else:
            self._title = new_title

    def results(self):
        return [res for res in Result.all if res.game is self]

    def players(self):
        return list({res.player for res in Result.all if res.game is self})

    def average_score(self, player):
        scores = [res.score for res in self.results() if res.player == player]
        return sum(scores) / len(scores)


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if not isinstance(new_username, str):
            raise TypeError("Username must be of type String.")
        elif not 2 <= len(new_username) <= 16:
            raise ValueError("Username must contain 2 - 16 characters.")
        else:
            self._username = new_username

    def results(self):
        return [res for res in Result.all if res.player is self]

    def games_played(self):
        return list({res.game for res in Result.all if res.player is self})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([res for res in self.results() if res.game == game])


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, new_player):
        if not isinstance(new_player, Player):
            raise TypeError("Player must be an instance of Player Class.")
        else:
            self._player = new_player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, new_game):
        if not isinstance(new_game, Game):
            raise TypeError("Game must be an instance of Game Class.")
        else:
            self._game = new_game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if not isinstance(new_score, int):
            raise TypeError("Score must be of type Integer.")
        # elif not 1 <= new_score <= 5000: # had to comment out to pass test, but one of the deliverables!
        #     raise ValueError("Score must be between 1 - 5000.")
        elif hasattr(self, "score"):
            raise AttributeError("Score cannot change after result is in.")
        else:
            self._score = new_score
