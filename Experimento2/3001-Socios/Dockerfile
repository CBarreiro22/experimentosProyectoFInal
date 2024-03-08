FROM python:3.10-alpine
WORKDIR /3002-Usuario
COPY requirements.txt .
COPY .env.development .
RUN pip install -r requirements.txt
COPY src /3002-Usuario/src
ENV ENV_FILE .env.development
EXPOSE 3002
CMD FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3002