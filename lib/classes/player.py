class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        
    def results(self, new_result=None):
        from classes.result import Result
        pass
    
    def games_played(self, new_game=None):
        from classes.game import Game
        pass
    
    def played_game(self, game):
        pass
    
    def num_times_played(self, game):
        pass
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
