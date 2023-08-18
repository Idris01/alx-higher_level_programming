#!/usr/bin/python3
"""Adds new state to the database

This module adds a new state to the database and prints
the id of the added state
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    # get arguments supplied in the command line
    _, username, password, db_name = sys.argv

    # create engine based on the supplied arguments
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = "Louisiana"
    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()
    query = session.query(State).filter(
            State.name == state_name).all()
    print(query[0].id)
