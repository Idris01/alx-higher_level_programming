#!/usr/bin/python3
"""Displays all cities with corresponding states
and id
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # get arguments supplied in the command line
    _, username, password, db_name = sys.argv

    # create engine based on the supplied arguments
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all()
    if query:
        for city, state in query:
            id, city_name, state_name = city.id, city.name, state.name
            print("{}: ({}) {}".format(state_name, id, city_name))
