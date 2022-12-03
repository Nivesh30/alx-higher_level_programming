#!/usr/bin/python3
"""
class definition of a State and an instance
Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    State class
    attribute id that represents a column
    of an auto-generated, unique integer
    attribute name that represents a column of a
    string with maximum 128 characters and can’t be null
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="all, delete")
