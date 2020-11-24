from Game import Game
from random import randint


class GuessGame(Game):
    def __init__(self, diff):
        self.diff = diff

    def generate_number(self):
        secret_number = randint(1, self.diff)
        return secret_number

    def get_guess_from_user(self):
        print("==>> --------------------- <<==")
        print("==>> Welcome to Guess Game <<==")
        print("==>> --------------------- <<==")
        print("Please try guessing a number between 1 to %d" % self.diff)
        while (True):
            try:
                num_from_user = int(input())
                if (num_from_user < 1 or num_from_user > self.diff):
                    raise ValueError()
                else:
                    break
            except ValueError:
                print("Must be a number between 1 to %d !!" % self.diff)

        return num_from_user

    @staticmethod
    def compare_results(secret_number, num_from_user):
        print(secret_number)
        print(num_from_user)
        if (secret_number == num_from_user):
            return True
        else:
            return False

    def play(self):
        rand_number = self.generate_number()
        num_from_user = self.get_guess_from_user()
        result = self.compare_results(rand_number, num_from_user)
        return result