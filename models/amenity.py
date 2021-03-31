#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Amenity(BaseModel, Base):
    """
    Amenity class creation
    """
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       backref='amenities')
    else:
        name = ""
