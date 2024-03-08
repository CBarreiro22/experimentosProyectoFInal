FROM python:3.10-alpine
WORKDIR /usuario
COPY requirements.txt .
COPY .env.development .
RUN pip install -r requirements.txt
COPY src /usuario/src
ENV ENV_FILE .env.development
EXPOSE 300
CMD FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3000