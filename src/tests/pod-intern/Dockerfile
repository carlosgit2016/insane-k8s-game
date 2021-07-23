FROM python:3.10.0b4-alpine3.14

ENV FLASK_APP hello

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py 

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask", "run" ]