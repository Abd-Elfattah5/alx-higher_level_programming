#!/usr/bin/python3
""" module for state class to link to sqlalchemy"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base




class City(Base):
    """
    City class that inherits from Base

    Attributes:
        id: Id city
        name: Name of city
        state_id: Id of state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
