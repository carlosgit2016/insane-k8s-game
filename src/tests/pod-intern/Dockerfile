FROM python:3.9.6

ENV FLASK_APP main

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py 

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]