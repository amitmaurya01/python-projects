import math
import random


class Player:
    def __init__(self, letter) -> None:
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass



class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        pass
