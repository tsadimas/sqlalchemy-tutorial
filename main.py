from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'my.sqlite')

Base = declarative_base()
engine = create_engine(connection_string, echo=True)
Session = scoped_session(sessionmaker())


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(30), unique=True, nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __str__(self):
        return f"<User username={self.username}, email={self.email}>"


Base.metadata.create_all(engine)
local_session = Session(bind=engine)
user1 = User(username="John", email="john@hua.gr")
local_session.add(user1)
local_session.commit()
