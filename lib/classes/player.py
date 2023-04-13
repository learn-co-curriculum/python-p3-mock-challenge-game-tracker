class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        return len([r for r in self._results if r.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        if cls.all:
            max_player = None
            max_score = 0
            for p in cls.all:
                if game.average_score(p) > max_score:
                    max_player = p
                    max_score = game.average_score(p)
            return max_player
        return None
        
