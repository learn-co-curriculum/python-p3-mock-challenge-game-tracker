# Mock Code Challenge - Game Tracker (Object Relationships)

For this assignment, we'll be working with a game tracking domain.

We have three models: `Game`, `Player`, and `Result`.

For our purposes, a `Game` has many `Result`s, a `Player` has many
`Result`s, and a `Result` belongs to a `Player` and to a `Game`.

`Game` - `Player` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

> **NOTE: A number of tests will be passing before you make any changes. Keep an
> eye on this number to make sure you're maintaining this app's functionality as
> you write new code!**

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Game

- `Game __init__(self, title)`
  - `Game` is initialized with a title (string)
  - Title **cannot be** changed after the `Game` is initialized
- `Game property title`
  - Returns the `Game`'s title
  - Titles must be strings greater than 0 characters
  - If you are using exceptions, uncomment lines 25-26 and 32-33 in
    `testing/game_test.py`.
    - `raise Exception` if setter fails

#### Player

- `Player __init__(self, username)`
  - `Player` is initialized with a username (string)
  - Usernames **can be** changed after the Player is initialized
- `Player property username`
  - Returns the Player's username
  - Usernames must be strings between 2 and 16 characters,
    inclusive.
  - If you are using exceptions, uncomment lines 25-29 in
    `testing/player_test.py`.
    - `raise Exception` if setter fails

#### Result

- `Result __init__(self, player, game, score)`
  - `Result` is initialized with a `Player` instance, a `Game` instance, and a
    score (number).
- `Result property score`
  - Returns the score for the `Result` instance
  - Scores must be integers between 1 and 5000, inclusive
    - If you are using exceptions, uncomment lines 20-30 in
    `testing/result_test.py`.
    - `raise Exception` if setter fails

### Object Relationship Attributes and Properties

#### Result

- `Result property player`
  - Returns the player for the Result
  - Players must be `Player` instances
  - `raise Exception` if setter fails
- `Result property game`
  - Returns the game that was played
  - Games must be `Game` instances
  - `raise Exception` if setter fails

#### Player

- `Player results(self, new_result=None)`
  - Adds new results to instance attribute `player._results` if `new_result`
    exists.
  - Returns a list of `Result` instances associated with the `Player` instance.
  - _You will need to call this method in `Result.__init__()`._
- `Player games_played(self)`
  - Returns a list of `Game` instances played by the `Player` instance.

#### Game

- `Game results(self, new_result=None)`
  - Adds new results to instance attribute `game._results` if `new_result`
    exists.
  - Returns a list of `Result` instances associated with the `Game` instance.
  - _You will need to call this method in `Result.__init__()`._
- `Game players(self, new_player=None)`
  - Adds new results to instance attribute `player._results` if `new_result`
    exists.
  - Returns a list of `Result` instances associated with the `Player` instance.
  - _You will need to call this method in `Result.__init__()`._

### Aggregate and Association Methods

#### Player

- `Player played_game(self, game)`
  - Returns `True` if the `Player` has played this `Game` (if there is a
    `Result` instance that has this `Player` and `Game`), returns `False`
    otherwise
- `Player num_times_played(self, game)`
  - Returns the number of times the `Player` instance has played (`Result`
    instance created) the `Game` instance

#### Game

- `Game average_score(self, player)`
  - Returns the average of all the player's scores for the `Game` instance
  - To average scores, add all result scores together for the player and divide
    by the total number of results for the player.

#### Bonus: Aggregate and Association Method

- `Player classmethod highest_scored(cls, game)`
  - Returns the `Player` instance with the highest average game score.
  - Returns `None` if there are no players.
  - _hint: will need a way to remember all `Player` objects_
  - _hint: do you have a method to get the average score on a game for a
    particular player?_
