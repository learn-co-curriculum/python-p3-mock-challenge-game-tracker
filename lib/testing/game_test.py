from classes.player import Player
from classes.game import Game
from classes.result import Result
import pytest


class TestGame:
    '''Game in game.py'''

    def test_has_title(self):
        '''game is initialized with a title'''
        game = Game("Skribbl.io")
        assert (game.title == "Skribbl.io")

    def test_title_is_string(self):
        '''game is initialized with a title of type str'''
        game = Game("Skribbl.io")
        assert (isinstance(game.title, str))

    def test_title_len(self):
        '''game is initialized with a title greater than 0 characters'''
        game = Game("Skribbl.io")
        assert (hasattr(game, "title"))

        game_2 = Game("")
        assert (not hasattr(game_2, "title"))

    def test_title_setter(self):
        '''Cannot change the title of the game'''
        game = Game("Skribbl.io")
        game.title = "not Skribbl.io"
        assert (game.title == "Skribbl.io")

    # def test_raise_exception_for_changing_title(self):
    #     '''raise exception for trying to change title after initialization'''
    #     game = Game("Skribbl.io")
    #     with pytest.raises(Exception):
    #         game.title = 'Banana'

    def test_has_many_results(self):
        '''Game has many results.'''
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player('Saaammmm')
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 3500)
        result_3 = Result(player, game_2, 19)

        assert (len(game.results()) == 2)
        assert (result_1 in game.results())
        assert (result_2 in game.results())
        assert (not result_3 in game.results())

    def test_results_of_type_result(self):
        '''game results are of type Result'''
        game = Game("Skribbl.io")
        player = Player('Saaammmm')
        Result(player, game, 2000)
        Result(player, game, 3500)

        assert (isinstance(game.results()[0], Result))
        assert (isinstance(game.results()[1], Result))

    def test_has_many_players(self):
        '''game has many players.'''
        game = Game("Skribbl.io")

        player = Player('Nick')
        player_2 = Player('Ari')
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert (player in game.players())
        assert (player_2 in game.players())

    def test_players_of_type_player(self):
        '''game players are of type player'''
        game = Game("Skribbl.io")
        player = Player('Nick')
        player_2 = Player('Ari')
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert (isinstance(game.players()[0], Player))
        assert (isinstance(game.players()[1], Player))

    def test_average_score(self):
        '''test average_score()'''
        game = Game("Skribbl.io")
        player = Player('Nick')
        Result(player, game, 5000)
        Result(player, game, 4999)
        Result(player, game, 5000)
        Result(player, game, 4999)

        assert (game.average_score(player) == 4999.5)
