FROM python:3-alpine

WORKDIR /app

COPY MainScores.py ./
COPY Score.py ./
COPY Utils.py ./
COPY score.txt ./
copy templates ./templates/
ADD requirements.txt ./

RUN pip install -r requirements.txt
RUN chmod -R 777 ./

EXPOSE 8777

CMD ["python", "MainScores.py"]