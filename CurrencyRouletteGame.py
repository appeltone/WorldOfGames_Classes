from Game import Game
from random import randint
import requests
import json
import os


class CurrencyRouletteGame(Game):
    def __init__(self, diff):
        self.diff = diff

    def get_money_interval(self):
        usd_random_amount = randint(1, 100)
        # Set Url
        # This should be a const of the entire currency class.
        url = 'https://v6.exchangerate-api.com/v6/5fc4a1b2d88ef290d6c188bb/latest/USD'

        # Get response from API url
        response = requests.get(url)

        # create Json object from all the response (type is dict)
        json_main_object = json.loads(response.text)

        # Get conversion rates dict/object (nested object) from main Json object
        conversion_rates_dict = json_main_object["conversion_rates"]

        # Get ILS current exchange rate
        ils_rate = conversion_rates_dict["ILS"]
        ils_from_usd = usd_random_amount * ils_rate

        return ils_from_usd - (5 - self.diff), ils_from_usd + (5 - self.diff), usd_random_amount

    @staticmethod
    def get_guess_from_user(generated_usd):
        os.system('cls')
        print("==>> --------------------------------- <<==")
        print("==>> Welcome to Currency Roulette Game <<==")
        print("==>> --------------------------------- <<==")
        print("The computer generated a random USD amount = %d " % generated_usd)
        print("Please guess the conversion amount in ILS: ")

        while (True):
            try:
                ils_guess_from_user = int(input())
                break
            except ValueError:
                print("Must be a number !!")

        return ils_guess_from_user

    def play(self):
        interval_low, interval_high, generated_usd = self.get_money_interval()
        ils_guess_from_user = self.get_guess_from_user(generated_usd)
        if interval_high > ils_guess_from_user > interval_low:
            return True
        else:
            return False

