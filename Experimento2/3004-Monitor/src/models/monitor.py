import uuid
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String
from src.models.model import Model, Base
from sqlalchemy_utils import UUIDType


class Monitor(Model, Base):
    __tablename__ = 'monitor'
    transaccion_uuid= Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    nombre_microservicio = Column(String(100))
    estado_microservicio = Column(String(100))
    contador= Column(Integer)
    def __init__(self, nombre_microservicio, estado_microservicio, contador):
        Model.__init__(self)
        self.nombre_microservicio = nombre_microservicio
        self.estado_microservicio = estado_microservicio
        self.contador = contador

class MonitorJsonSchema(Schema):
    id = fields.UUID()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    transaccion_uuid = fields.UUID()
    nombre_microservicio = fields.String()
    estado_microservicio = fields.String()
    contador = fields.Integer()
    class Meta:
        fields = ('id', 'created_at', 'updated_at', 'transaccion_uuid', 'nombre_microservicio', 'estado_microservicio', 'contador')