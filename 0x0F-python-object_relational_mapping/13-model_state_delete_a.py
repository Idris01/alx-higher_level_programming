#!/usr/bin/python3
"""Delete all states with names that contain 'a'
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
            State.name.contains('a')).all()
    if query:
        for item in query:
            session.delete(item)
        session.commit()
