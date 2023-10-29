import pytest

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result


class TestResults:
    """Result in many_to_many.py"""

    def test_has_score(self):
        """Result is initialized with a score"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 5000)

        assert result_1.score == 2000
        assert result_2.score == 5000

    def test_score_is_immutable_int(self):
        """result score is an immutable integer"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result_1 = Result(player, game, 2000)
        assert isinstance(result_1.score, int)

        # comment out the next three lines if using Exceptions
        # result_1.score = 5000
        # assert result_1.score == 2000
        # assert isinstance(result_1.score, int)

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Result(player, game, "500")

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Result(player, game, 400.99)

    def test_score_is_valid(self):
        """score is between 1 and 5000 inclusive"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        result = Result(player, game, 5000)

        assert 1 <= result.score <= 5000

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            result.score = 5001

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            result.score = 0

    def test_has_a_player(self):
        """result has a player"""
        game = Game("Skribbl.io")
        player_1 = Player("Tricia")
        player_2 = Player("Bianca")
        result_1 = Result(player_1, game, 3000)
        result_2 = Result(player_2, game, 3000)

        assert result_1.player == player_1
        assert result_2.player == player_2

    def test_player_of_type_player(self):
        """player is of type Player"""
        game = Game("Scattegories")
        player = Player("Kyle")
        player_2 = Player("Brett")
        result_1 = Result(player, game, 9)
        result_2 = Result(player_2, game, 10)

        assert isinstance(result_1.player, Player)
        assert isinstance(result_2.player, Player)

    def test_has_a_game(self):
        """result has a game"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player_1 = Player("Ja'Vonn")
        result_1 = Result(player_1, game_1, 8)
        result_2 = Result(player_1, game_2, 3000)

        assert result_1.game == game_1
        assert result_2.game == game_2

    def test_game_of_type_game(self):
        """game is of type Game"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player = Player("Kyle")
        result_1 = Result(player, game_1, 2000)
        result_2 = Result(player, game_2, 5000)

        assert isinstance(result_1.game, Game)
        assert isinstance(result_2.game, Game)

    def test_get_all_results(self):
        """Result class has all attribute"""
        Result.all = []
        game = Game("Codenames")
        player_1 = Player("Ja'Vonn")
        player_2 = Player("Brett")
        result_1 = Result(player_1, game, 2)
        result_2 = Result(player_2, game, 5)

        assert len(Result.all) == 2
        assert result_1 in Result.all
        assert result_2 in Result.all
