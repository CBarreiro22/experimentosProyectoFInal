FROM python:3.10-alpine
WORKDIR /Deportista
COPY requirements.txt .
COPY .env.development .
RUN pip install -r requirements.txt
COPY src /Deportista/src
ENV ENV_FILE .env.development
EXPOSE 3001
CMD FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3001
