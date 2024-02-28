import datetime
from sqlalchemy import Column, String, DateTime
from .model import Model


class Sportsman(Model):
    __tablename__ = 'sportsman'
    STATUS_CHOICES = ("POR_VERIFICAR", "NO_VERIFICADO", "VERIFICADO")

    name = Column(String(64), nullable=False)
    last_name = Column(String(128), nullable=False)
    kind_of_identification = Column(String(64), nullable=True)
    number_identification = Column(String(12), nullable=True)
    # full_name = Column(String(64), nullable=True)
    # password = Column(String(128), nullable=False)
    # salt = Column(String(128), nullable=False)
    # token = Column(String(128), nullable=True)
    # status = Column(String(128), default="POR_VERIFICAR")
    # expireAt = Column(DateTime, default=datetime.datetime.utcnow)
    #
    # def __init__(self, username, password, salt, email, phone_number=None, dni=None, full_name=None):
    #     self.username = username
    #     self.password = password
    #     self.salt = salt
    #     self.email = email
    #     self.phone_number = phone_number
    #     self.dni = dni
    #     self.full_name = full_name
    #
    #     super().__init__()