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
    if getenv('HBNB_TYPE_STORAGE' == 'db'):
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       backref='amenities')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Amenity class initialization
        """
        super().__init__(*args, **kwargs)
