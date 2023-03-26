#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
		"Review", backref="places", cascade="delete")
        amenities = relationship(
		"Amenity", secondary="place_amenity", overlaps="place_amenities", viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            my_list = []
            for i in storage.all(Review):
                if self.id == i.place_id:
                    my_list.append(i)
            return my_list

        @property
        def amenities(self):
            from models import storage
            my_list = []
            for i in storage.all(Amenity).values():
                if i.id in self.amenity_ids:
                    my_list.append(i)
            return my_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
