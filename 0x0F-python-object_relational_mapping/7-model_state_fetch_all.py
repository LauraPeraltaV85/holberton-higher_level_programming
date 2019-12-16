#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhos\
t/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
new_states = session.query(State).order_by(State.id).all()
for state in new_states:
    print("{}: {}".format(state.id, state.name))
session.close()
