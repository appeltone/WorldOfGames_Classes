from flask import Flask, request, render_template
from Score import get_score_from_file
from Utils import *
from os import path

app = Flask(__name__)


@app.route('/', methods=["GET"])
def score_server():
    if (path.exists(SCORES_FILE_NAME)):
        current_score_from_file = get_score_from_file(SCORES_FILE_NAME)
        if (current_score_from_file != ''):
            return render_template('validHTML.html', SCORE=current_score_from_file)
        else:
            return render_template('ErrorHTML.html', ERROR=FILE_EMPTY_ERROR)
    else:
        return render_template('ErrorHTML.html', ERROR=FILE_NOT_FOUND_ERROR)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8777)
