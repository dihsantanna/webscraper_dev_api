FROM python:3.10.6-slim-buster

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./src/index.py"]