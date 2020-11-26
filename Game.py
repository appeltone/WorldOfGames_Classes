""" this abstract class will force any game who inherits from it to implement the play method"""
from abc import ABC, abstractmethod


class Game(ABC):

    # I would also move the "get_X_from_user" methods here too. you have them in all 3 games, so make it structured here


    @abstractmethod
    def play(self):
        pass
