#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
