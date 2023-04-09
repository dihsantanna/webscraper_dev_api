# syntax=docker/dockerfile:1

FROM ubuntu:focal

FROM python:3.11.3-slim-bullseye

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip 

RUN pip3 install -r requirements.txt

RUN playwright install --with-deps chromium

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]