from Live import load_game, welcome
#
# General comments:
#
# * What about making this a python package so i can just run "pip install" and it will install the game - good practice and challange
# * If you want to take it further- you can add a "common" module, that will have generic functions like: string manipulation, input validation etc,
# and then simply calling it when ever you want and not checking the same thing in all the files


print(welcome("Appel Eran"))
load_game()
