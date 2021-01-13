""" this abstract class will force any game who inherits from it to implement the play method"""
import os
from abc import ABC, abstractmethod


class Game(ABC):

    @abstractmethod
    def generate_number(self):
        pass

    @abstractmethod
    def get_guess_from_user(self):
        pass

    @abstractmethod
    def play(self):
        pass
