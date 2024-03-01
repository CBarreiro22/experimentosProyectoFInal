import uuid
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_utils import UUIDType

from models.model import Model, Base


class Partner(Model, Base):
    __tablename__ = 'partner'
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    serviceTypeId = Column(String, nullable=False)
    regionId = Column(String, nullable=False)
    countryId = Column(String, nullable=False)
    city = Column(String, nullable=False)
    partnerId = Column(Integer, nullable=False)

    def __init__(self, name, description, price, serviceTypeId, regionId, countryId, city, partnerId):
        Model.__init__(self)
        self.name = name
        self.description = description
        self.price = float(price)
        self.serviceTypeId = serviceTypeId
        self.regionId = regionId
        self.countryId = countryId
        self.city = city
        self.partnerId = partnerId


class PartnerJsonSchema(Schema):
    id = fields.UUID()
    name = fields.String()
    description = fields.String()
    price = fields.Float()
    serviceTypeId = fields.String()
    regionId = fields.String()
    countryId = fields.String()
    city = fields.String()
    partnerId = fields.Integer()
    created_at = fields.DateTime()

    class Meta:
        fields = ('id', 'name', 'description', 'price', 'serviceTypeId', 'regionId',
                  'countryId', 'city', 'partnerId', 'created_at')
