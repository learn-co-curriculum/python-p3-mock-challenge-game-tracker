from classes.player import Player
from classes.game import Game
from classes.result import Result
import pytest


class TestResults:
    '''Result in result.py'''

    def test_has_score(self):
        '''is initialized with a score'''
        game = Game("Skribbl.io")
        player = Player('Nick')
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 5000)

        assert (result_1.score == 2000)
        assert (result_2.score == 5000)

    # def test_raise_exception_for_invalid_score(self):
    #     '''raise exception when invalid score'''
    #     game = Game("Skribbl.io")
    #     player = Player('Nick')
    #     result = Result(player, game, 2000)
    #     with pytest.raises(Exception):
    #         result.score = 6000
    #     with pytest.raises(Exception):
    #         result.score = "500"
    #     with pytest.raises(Exception):
    #         result.score = -3

    def test_has_a_player(self):
        '''result has a player .'''
        game = Game("Skribbl.io")
        player_1 = Player('Tricia')
        player_2 = Player('Bianca')
        result_1 = Result(player_1, game, 3000)
        result_2 = Result(player_2, game, 3000)

        assert (result_1.player == player_1)
        assert (result_2.player == player_2)

    def test_player_of_type_player(self):
        '''player is of type Player'''
        game = Game("Scattegories")
        player = Player("Kyle")
        result_1 = Result(player, game, 9)
        print("All the participation points!")
        result_2 = Result(player, game, 10)

        assert (isinstance(result_1.player, Player))
        assert (isinstance(result_2.player, Player))

    def test_has_a_game(self):
        '''result has a game.'''
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player_1 = Player("Ja'Vonn")
        result_1 = Result(player_1, game_2, 8)
        result_2 = Result(player_1, game_1, 3000)

        assert (result_1.game == game_2)
        assert (result_2.game == game_1)

    def test_game_of_type_game(self):
        '''game is of type Game'''
        game = Game("Skribbl.io")
        player = Player('Kyle')
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 5000)

        assert (isinstance(result_1.game, Game))
        assert (isinstance(result_2.game, Game))

    def test_get_all_results(self):
        '''test Result class all attribute'''
        Result.all = []
        game = Game("Codenames")
        player = Player("Ja'Vonn")
        player_2 = Player("Brett")
        result_1 = Result(player, game, 2)
        result_2 = Result(player_2, game, 5)

        assert (len(Result.all) == 2)
        assert (result_1 in Result.all)
        assert (result_2 in Result.all)
