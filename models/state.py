#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
import models
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.city import City
from models.place import Place
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initalization of State class
        """
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            cities_list = []
            dict_cities = models.storage.all(City)
            for key, city in dict_cities.items():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
