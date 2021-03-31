#!/usr/bin/python3
""" Place Module for HBNB project """
import models
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.review import Review
from os import getenv
from models.amenity import Amenity

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', secondary='place_amenity',
                             backref='places', viewonly=False)

    @property
    def review(self):
        """
        Returns instance of the reviews
        """
        review_list = []
        review_obj = models.storage.all(Review)
        for review in review_obj.values():
            if review.place_id is self.id:
                review_list.append(review)

        return review_list

    @property
    def amenities(self):
        """
        Return instance of the amenities
        """
        amenity_list = []
        amenity_obj = models.storage.all(Amenity)
        for amenity in amenity_obj.values():
            if amenity.id in self.amenity_ids:
                amenity_list.append(amenity)

        return amenity_list

    @amenities.setter
    def amenities(self, obj=None):
        """
        Setter for amenity instance
        """
        if type(obj) == Amenity:
            self.amenity_ids.append(obj.id)
        else:
            pass
