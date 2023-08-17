#!/usr/bin/python3
"""Query database for all names that contain 'a'

This Module define a script that get the names and id of
states that contain letter 'a'
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
    query = session.query(State).filter(
            State.name.contains('A')
            ).order_by(State.id).all()
    for item in query:
        print("{}: {}".format(item.id, item.name))
