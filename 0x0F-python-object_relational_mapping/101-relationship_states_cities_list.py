#!/usr/bin/python3
"""List all states and corresponding cities

of database hbtn_0e_101_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    _, user, password, db_name = sys.argv
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                user, password, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    if query:
        query = query.all()
        for state in query:
            id, name = state.id, state.name
            print("{}: {}".format(id, name))
            for city in state.cities:
                city_id, city_name = city.id, city.name
                print("\t{}: {}".format(city_id, city_name))
