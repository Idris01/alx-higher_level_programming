#!/usr/bin/python3
"""Define an ORM model for state Model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Define a State model

    The State model represents ORM for state database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', backref="state", cascade="all, delete, delete-orphan")
