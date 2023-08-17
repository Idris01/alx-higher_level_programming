#!/usr/bin/python3
"""Query All name module

This Module define a script that query all names of a given
database in ascending order of id
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
    query = session.query(State.name).order_by(State.id).all()
    for index, item in enumerate(query):
        print("{}: {}".format(index + 1, item[0]))
