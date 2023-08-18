#!/usr/bin/python3
"""Update the name of state with id 2

This module update the name of of state with id
to "New Mexico
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
    new_name = "New Mexico"

    query = session.query(State).filter(
            State.id == 2).all()
    if query:
        query = query[0]
        query.name = new_name
        session.add(query)
        session.commit()
