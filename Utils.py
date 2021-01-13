import os

SCORES_FILE_NAME = "./score.txt"
BAD_RETURN_CODE = "oopsy, somethinig went wrong"
FILE_NOT_FOUND_ERROR = "The file was not found!! damn"
FILE_EMPTY_ERROR = "There is no scores yet dummy !!!"


def clean_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
