#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, base
from sqlalchemy import Column, String, FreignKey

class Review(BaseModel, base):
    """ Review class to store review information """

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False, )
    text = Column(String(1024), nullable=False)
