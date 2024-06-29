#!/usr/bin/python3
""" using sqlalchemy to query date """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    Base.metadata.create_all(engine)

    state = session.query(State).filter(id='2').first()
    state.name = "New Mexico"
    session.commit()
    session.close()
