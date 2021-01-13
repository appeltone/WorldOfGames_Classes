from Utils import *
from os import path


def add_score(diff):
    current_score = ''
    new_score = ''
    # open file for writting in append mode if exist
    if (path.exists(SCORES_FILE_NAME)):
        current_score = get_score_from_file(SCORES_FILE_NAME)
        if (current_score != ''):
            new_score = int(current_score) + (diff * 3) + 5
        else:
            new_score = (diff * 3) + 5
        f = open(SCORES_FILE_NAME, "w", encoding='utf-8')
        f.write(str(new_score))
    else:
        f = open(SCORES_FILE_NAME, "x", encoding='utf-8')
        f.write(str((diff * 3) + 5))
    f.close()


def get_score_from_file(file_path):
    try:
        f = open(SCORES_FILE_NAME, 'r')
        score = f.readline()
        return score
    except:
        print(" File cannot be found")
    finally:
        f.close()
