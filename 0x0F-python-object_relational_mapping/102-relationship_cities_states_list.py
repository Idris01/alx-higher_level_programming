#!/usr/bin/python3
"""List all cities  and corresponding states

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
    query = session.query(City).order_by(City.id)
    if query:
        query = query.all()
        for city in query:
            id, name, state = city.id, city.name, city.state.name
            print("{}: {} -> {}".format(id, name, state))
