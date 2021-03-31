#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', secondary='place_amenity',
                             backref='places', viewonly=False)

    @property
    def reviews(self):
        """Getter for Review instances"""
        list_review = []
        dict_review = models.storage.all(Review)
        for review in dict_review.values():
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    @property
    def amenities(self):
        """Getter for Amenity instances"""
        list_amenities = []
        dict_amenities = models.storage.all(Amenity)
        for amenity in dict_amenities.values():
            if amenity.id in self.amenity_ids:
                list_amenities.append(amenity)
        return list_amenities

    @amenities.setter
    def amenities(self, obj):
        """Setter for Amenity instances"""
        if type(obj) == Amenity:
            self.amenity_ids.append(obj.id)
