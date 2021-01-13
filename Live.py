from MemoryGame import *
from GuessGame import *
from CurrencyRouletteGame import *
import os
from Score import add_score
from Utils import clean_screen


def welcome(name):
    return "Hello " + name + " and wecome to the World Of Games (WoG).\n" + "Here you can find cool Games to play.\n"\
           + "---------------------------------------------------"


def load_game():
    clean_screen()
    # print header for game selection
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print("Enter Selection:")
    while (True):
        try:
            game_slected = int(input())
            if (
                    game_slected <= 3 and game_slected >= 1):
                break
            else:
                raise ValueError()
        except ValueError:
            print("Must be a number between 1 to 3 !!")
    clean_screen()
    print("Please choose game difficulty from 1 to 5:")
    print("Enter Selection:")
    while (True):
        try:
            diff = int(input())
            if (diff < 1 or diff > 5):
                os.system('cls')
                raise ValueError()
            else:
                os.system('cls')
                break
        except ValueError:
            print("Must be a number between 1 to 5 !!")

    if game_slected == 1:
        memory_game = MemoryGame(diff)
        if (memory_game.play()):
            print("Yeeppee... YOU WON")
            print("Updating score file...")
            add_score(diff)
        else:
            print("Sorry... YOU LOSE")
    elif game_slected == 2:
        guess_game = GuessGame(diff)
        if (guess_game.play()):
            print("Yeeppee... YOU WON")
            print("Updating score file...")
            add_score(diff)
        else:
            print("Sorry... YOU LOSE")
    elif game_slected == 3:
        currency_game = CurrencyRouletteGame(diff)
        if (currency_game.play()):
            print("Yeeppee... YOU WON")
            print("Updating score file...")
            add_score(diff)
        else:
            print("Sorry... YOU LOSE")
