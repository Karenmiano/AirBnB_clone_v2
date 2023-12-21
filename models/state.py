#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import environ

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Returns all cities in the state"""
        all_cities = models.storage.all(City)
        state_cities = []
        for obj in all_cities.values():
            if obj.state_id == self.id:
                state_cities.append(obj)
        return state_cities
