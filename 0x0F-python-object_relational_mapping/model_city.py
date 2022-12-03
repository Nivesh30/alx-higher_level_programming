#!/usr/bin/python3
"""
class definition of a city and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    State class
    attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key

    attribute name that represents a column of a
    string of 128 characters and can’t be null
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
