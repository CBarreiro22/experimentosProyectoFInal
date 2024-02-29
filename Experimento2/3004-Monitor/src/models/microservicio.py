import time
import requests

class Microservice:
    def __init__(self, name, limit, url) -> None:
        self.name = name
        self.status = "OK"
        self.status_description = "Servicio en buen estado"
        self.contador = 0
        self.limit = limit
        self.last_check = time.time()
        self.url = url
    
    def increment(self):
        self.contador += 1
    
    def reset(self):
        self.contador = 0
        self.status = "OK"
        self.status_description = "Servicio en buen estado"
        self.last_check = time.time()
    
    def is_alive(self):
        if self.contador >= self.limit:
            self.status = "ERROR"
            self.status_description = "Servicio no disponible"
        return self.status
    
    def check(self):
        try:
            response = requests.get(self.url).status_code
        except requests.exceptions.RequestException as e:
            response = 500
        if response != 200:
            self.increment()
        return self.is_alive()
      