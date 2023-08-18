#!/usr/bin/python3
"""Query database for state with the given name

This Module define a script that prints the id of the state
with the given name
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    # get arguments supplied in the command line
    _, username, password, db_name, state_name = sys.argv

    # create engine based on the supplied arguments
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(
            State.name == state_name).all()
    if query:
        print(query[0].id)
    else:
        print("Not found")
