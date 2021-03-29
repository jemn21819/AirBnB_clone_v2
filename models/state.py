#!/usr/bin/python3
""" State Module for HBNB project """
import sqlalchemy
import models
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models.city import City
from models.place import Place


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(State(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

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
