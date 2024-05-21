#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute of cities that returns the list of City"""
        from models import storage
        my_list = []
        citiesExtracts = storage.all(City).values()
        for city in citiesExtracts:
            if self.id == city.state_id:
                my_list.append(city)
        return my_list
