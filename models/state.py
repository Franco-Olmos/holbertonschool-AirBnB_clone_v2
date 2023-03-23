#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    env = os.getenv('HBNB_TYPE_STORAGE')
    if env != 'db':
        @property
        def cities(self):
            from models import storage
            return [key for key, value in storage.all(City).items()
                    if self.id == value.state_id]
