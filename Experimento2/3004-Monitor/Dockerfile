FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
COPY .env.development .

RUN pip install -r requirements.txt

COPY src /app/src

EXPOSE 3000

CMD FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3000