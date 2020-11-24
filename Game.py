""" this abstract class will force any game who inherits from it to implement the play method"""
from abc import ABC, abstractmethod


class Game(ABC):

    @abstractmethod
    def play(self):
        pass
