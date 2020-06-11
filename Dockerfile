FROM python:3.7

WORKDIR /app

RUN pip install pip-tools

COPY app/requirements.in /app/requirements.in
COPY app/requirements.txt /app/requirements.txt

RUN pip-sync

COPY app /app
