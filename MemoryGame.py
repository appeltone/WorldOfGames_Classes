from Game import Game
from random import randint
import os
import time
from Utils import clean_screen


class MemoryGame(Game):
    def __init__(self, diff):
        self.diff = diff

    def generate_number(self):
        generated_numbers = []
        for number in range(self.diff):
            generated_numbers.append(randint(1, 101))
        return generated_numbers

    def get_guess_from_user(self, generated_list):
        nums_from_user = []
        clean_screen()
        print("==>> ---------------------- <<==")
        print("==>> Welcome to Memory Game <<==")
        print("==>> ---------------------- <<==")
        print("You will be shown %d numbers, try and remember them before they are gone :-)" % self.diff)
        input("Press any key when ready to start...")
        clean_screen()
        print(generated_list)
        time.sleep(2)
        clean_screen()
        print("Please try and type in the numbers that were shown to you (%d numbers)" % self.diff)
        input("Press any key when ready to start...")
        clean_screen()
        for i in range(1, self.diff + 1):
            while (True):
                try:
                    num_from_user = int(input("Number %d: " % i))
                    if (num_from_user < 1 or num_from_user > 101):
                        clean_screen()
                        raise ValueError()
                    else:
                        nums_from_user.append(num_from_user)
                        clean_screen()
                        break
                except ValueError:
                    print("Must be a number between 1 to 101 !!")

        return nums_from_user

    @staticmethod
    def is_list_equal(list_generated, list_from_user):
        if (list_generated == list_from_user):
            return True
        else:
            return False

    def play(self):
        generated_list = self.generate_number()
        list_from_user = self.get_guess_from_user(generated_list)
        print(generated_list)
        print(list_from_user)
        return (self.is_list_equal(generated_list, list_from_user))
