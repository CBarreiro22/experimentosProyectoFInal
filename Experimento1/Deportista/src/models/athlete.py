from sqlalchemy import Column, String, DateTime
from .model import Model
from sqlalchemy import Enum, Integer


class Athlete(Model):
    __tablename__ = 'athlete'
    STATUS_CHOICES = ("POR_VERIFICAR", "NO_VERIFICADO", "VERIFICADO")

    name = Column(String(64), nullable=False)
    last_name = Column(String(128), nullable=False)
    kind_of_identification = Column(Enum("Cedula", "Identificacion", "Pasaporte"), nullable=True)
    number_identification = Column(String(12), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(Enum("M", "F", "O"), nullable=True)
    country_of_birth = Column(String(64), nullable=True)
    city_of_birth = Column(String(64), nullable=True)
    country_of_residence = Column(String(64), nullable=True)
    city_of_residence = Column(String(64), nullable=True)
    length_of_residence = Column(Integer, nullable=True)
    sport_you_practice_or_wish_to_practice = Column(String(64), nullable=True)

    def __init__(self, name,
                 last_name, kind_of_identification, number_identification,
                 age, gender, country_of_birth,city_of_birth, country_of_residence,
                 city_of_residence,length_of_residence,sport_you_practice_or_wish_to_practice):
        self.name = name
        self.last_name = last_name
        self.kind_of_identification = kind_of_identification
        self.number_identification = number_identification
        self.age = age
        self.gender = gender
        self.country_of_birth = country_of_birth
        self.city_of_birth = city_of_birth
        self.country_of_residence = country_of_residence
        self.city_of_residence = city_of_residence
        self.length_of_residence = length_of_residence
        self.sport_you_practice_or_wish_to_practice = sport_you_practice_or_wish_to_practice

        super().__init__()
