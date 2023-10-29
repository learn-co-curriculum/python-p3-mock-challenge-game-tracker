import pytest

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result


class TestGame:
    """Game in many_to_many.py"""

    def test_has_title(self):
        """Game is initialized with a title"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Jenga")

        assert game_1.title == "Skribbl.io"
        assert game_2.title == "Jenga"

    def test_title_is_immutable_string(self):
        """title is an immutable string"""
        game = Game("Skribbl.io")
        assert isinstance(game.title, str)

        # comment out the next two lines if using Exceptions
        # game.title = 2
        # assert game.title == "Skribbl.io"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            game.title = "not Skribbl.io"

    def test_title_len(self):
        """title is greater than 0 characters"""
        game = Game("Skribbl.io")

        assert hasattr(game, "title")
        assert len(game.title) > 0

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Game("")

    def test_has_many_results(self):
        """game has many results"""
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player("Saaammmm")
        result_1 = Result(player, game, 2000)
        result_2 = Result(player, game, 3500)
        result_3 = Result(player, game_2, 19)

        assert len(game.results()) == 2
        assert result_1 in game.results()
        assert result_2 in game.results()
        assert result_3 not in game.results()

    def test_results_of_type_result(self):
        """game results are of type Result"""
        game = Game("Skribbl.io")
        player = Player("Saaammmm")
        Result(player, game, 2000)
        Result(player, game, 3500)

        assert isinstance(game.results()[0], Result)
        assert isinstance(game.results()[1], Result)

    def test_has_many_players(self):
        """game has many players"""
        game = Game("Skribbl.io")

        player = Player("Nick")
        player_2 = Player("Ari")
        player_3 = Player("Saaammmm")
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert player in game.players()
        assert player_2 in game.players()
        assert player_3 not in game.players()

    def test_players_of_type_player(self):
        """game players are of type Player"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        player_2 = Player("Ari")
        Result(player, game, 5000)
        Result(player_2, game, 4999)

        assert isinstance(game.players()[0], Player)
        assert isinstance(game.players()[1], Player)

    def test_has_unique_players(self):
        """game players are unique"""
        game = Game("Skribbl.io")

        player = Player("Nick")
        player_2 = Player("Ari")
        Result(player, game, 5000)
        Result(player, game, 5002)
        Result(player_2, game, 4999)

        assert len(set(game.players())) == len(game.players())
        assert len(game.players()) == 2

    def test_average_score(self):
        """game can calculate a player's average score"""
        game = Game("Skribbl.io")
        player = Player("Nick")
        Result(player, game, 5000)
        Result(player, game, 4999)
        Result(player, game, 5000)
        Result(player, game, 4999)

        assert game.average_score(player) == 4999.5
