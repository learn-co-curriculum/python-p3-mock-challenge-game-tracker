import pytest

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result


class TestPlayer:
    """Player in many_to_many.py"""

    def test_has_username(self):
        """Player is initialized with an username"""
        player = Player("Saaammmm")
        assert player.username == "Saaammmm"

    def test_username_is_mutable_string(self):
        """username is of type str and can change"""
        player = Player("Saaammmm")
        assert isinstance(player.username, str)

        player.username = "ActuallyTopher"
        assert player.username == "ActuallyTopher"

        # comment out the next two lines if using Exceptions
        # player.username = 2
        # assert player.username == "ActuallyTopher"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            player.username = 2

    def test_title_len(self):
        """username is between characters 2 and 16 characters long"""
        player = Player("Saaammmm")

        assert hasattr(player, "username")
        assert 2 <= len(player.username) <= 16

        # comment out the next two lines if using Exceptions
        # player.username = "y"
        # assert player.username == "Saaammmm"

        # comment out the next two lines if using Exceptions
        # player.username = "this_username_is_too_long"
        # assert player.username == "Saaammmm"

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Player("y")

        # uncomment the next two lines if using Exceptions
        with pytest.raises(Exception):
            Player("this_username_is_too_long")

    def test_has_many_results(self):
        """player has many results"""
        game = Game("Skribbl.io")
        player_1 = Player("Saaammmm")
        player_2 = Player("ActuallyTopher")
        result_1 = Result(player_1, game, 2000)
        result_2 = Result(player_1, game, 3500)
        result_3 = Result(player_2, game, 190)

        assert len(player_1.results()) == 2
        assert result_1 in player_1.results()
        assert result_2 in player_1.results()
        assert result_3 not in player_1.results()
        assert result_3 in player_2.results()

    def test_results_of_type_result(self):
        """player results are of type Result"""
        game = Game("Skribbl.io")
        player = Player("Saaammmm")
        Result(player, game, 2000)
        Result(player, game, 3500)

        assert isinstance(player.results()[0], Result)
        assert isinstance(player.results()[1], Result)

    def test_has_many_games(self):
        """player has many games played"""
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        game_3 = Game("Codenames")

        player_1 = Player("Nick")
        player_2 = Player("Saaammm")
        Result(player_1, game, 5000)
        Result(player_2, game_2, 19)
        Result(player_1, game_3, 10)

        assert game in player_1.games_played()
        assert game_2 not in player_1.games_played()
        assert game_3 in player_1.games_played()
        assert game_2 in player_2.games_played()

    def test_games_of_type_game(self):
        """player's games played are of type Game"""
        game = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player = Player("Ari")
        Result(player, game, 5000)
        Result(player, game_2, 17)

        assert isinstance(player.games_played()[0], Game)
        assert isinstance(player.games_played()[1], Game)

    def test_games_are_unique(self):
        """players keeps list of unique games played"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Codenames")
        player = Player("Nick")
        Result(player, game_1, 5000)
        Result(player, game_2, 19)
        Result(player, game_1, 100)

        assert len(set(player.games_played())) == len(player.games_played())
        assert len(player.games_played()) == 2

    def test_has_played_game(self):
        """player knows if a game has been played"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player_1 = Player("Saaammmm")
        player_2 = Player("ActuallyTopher")
        Result(player_1, game_1, 2000)
        Result(player_1, game_2, 3500)
        Result(player_2, game_1, 190)

        assert player_1.played_game(game_1) == True
        assert player_1.played_game(game_2) == True
        assert player_2.played_game(game_1) == True
        assert player_2.played_game(game_2) == False

    def test_has_num_times_played(self):
        """player knows how many times a game has been played"""
        game_1 = Game("Skribbl.io")
        game_2 = Game("Scattegories")
        player_1 = Player("Saaammmm")
        player_2 = Player("ActuallyTopher")
        Result(player_1, game_1, 2000)
        Result(player_1, game_2, 19)
        Result(player_1, game_1, 1900)
        Result(player_2, game_2, 9)

        assert player_1.num_times_played(game_1) == 2
        assert player_1.num_times_played(game_2) == 1
        assert player_2.num_times_played(game_1) == 0
        assert player_2.num_times_played(game_2) == 1

    # def test_highest_score(self):
    #     '''Player class finds player with highest average score for a given game'''
    #     game = Game("Skribbl.io")
    #     player_1 = Player('Saaammmm')
    #     player_2 = Player('ActuallyTopher')
    #     Result(player_1, game, 2000)
    #     Result(player_1, game, 1)
    #     Result(player_2, game, 1900)
    #     Result(player_2, game, 10)

    #     assert Player.highest_scored(game) == player_1
