import pytest

from classes.player import Player
from classes.game import Game
from classes.result import Result

class TestPlayer:
    '''Player in player.py'''

    def test_has_username(self):
        '''player is initialized with an username'''
        player = Player("Saaammmm")
        assert (player.username == "Saaammmm")

    def test_username_is_string(self):
        '''player is initialized with a username of type str'''
        player = Player("Saaammmm")
        assert (isinstance(player.username, str))

    def test_title_len(self):
        '''player is initialized with a username between characters 2 and 16 characters'''
        player = Player("Saaammmm")
        assert (hasattr(player, "username"))

        # with pytest.raises(Exception):
        #     Player("y")

        # with pytest.raises(Exception):
        #     Player("this_username_is_too_long")

    def test_username_setter(self):
        '''Can change the player's username'''
        player = Player("Saaammmm")
        player.username = "ActuallyTopher"
        assert (player.username == "ActuallyTopher")

    def test_has_many_results(self):
        '''Player has many results.'''
        game = Game("Skribbl.io")
        player = Player('Saaammmm')
        player_2 = Player('ActuallyTopher')
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 3500)
        result_3 = Result(player_2, game, 190)

        assert (len(player.results()) == 2)
        assert (result_1 in player.results())
        assert (result_2 in player.results())
        assert (not result_3 in player.results())

    def test_results_of_type_result(self):
        '''player results are of type Result'''
        game = Game("Skribbl.io")
        player = Player('Saaammmm')
        Result(player, game, 2000)
        Result(player, game, 3500)

        assert (isinstance(player.results()[0], Result))
        assert (isinstance(player.results()[1], Result))

    def test_has_many_players(self):
        '''Player has many games played.'''
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        game_3 = Game("Codenames")

        player = Player('Nick')
        player_2 = Player('Saaammm')
        Result(player, game, 5000)
        Result(player_2, game_2, 19)
        Result(player, game_3, 10)

        assert (game in player.games_played())
        assert (game_3 in player.games_played())
        assert (not game_2 in player.games_played())

    def test_games_of_type_game(self):
        '''Player's games played are of type Game'''
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player('Ari')
        Result(player, game, 5000)
        Result(player, game_2, 17)

        assert (isinstance(player.games_played()[0], Game))
        assert (isinstance(player.games_played()[1], Game))

    def test_has_played_game(self):
        '''Player has played the game.'''
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player('Saaammmm')
        player_2 = Player('ActuallyTopher')
        Result(player, game, 2000)
        Result(player, game_2, 3500)
        Result(player_2, game, 190)

        assert (player.played_game(game) == True)
        assert (player.played_game(game_2) == True)
        assert (player_2.played_game(game) == True)
        assert (player_2.played_game(game_2) == False)

    def test_has_num_times_played(self):
        '''how many times has the player played the game'''
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player('Saaammmm')
        player_2 = Player('ActuallyTopher')
        Result(player, game, 2000)
        Result(player, game_2, 19)
        Result(player, game, 1900)
        Result(player_2, game_2, 9)

        assert (player.num_times_played(game) == 2)
        assert (player.num_times_played(game_2) == 1)
        assert (player_2.num_times_played(game) == 0)
        assert (player_2.num_times_played(game_2) == 1)

    # def test_highest_score(self):
    #     '''which player has the highest average score for a given game'''
    #     game = Game("Skribbl.io")
    #     player = Player('Saaammmm')
    #     player_2 = Player('ActuallyTopher')
    #     Result(player, game, 2000)
    #     Result(player, game, 19)
    #     Result(player, game, 1900)
    #     Result(player_2, game, 9)

    #     assert Player.highest_scored(game) == player
