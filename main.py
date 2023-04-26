from __future__ import annotations
from sqlalchemy import String, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, Mapped, mapped_column, relationship, DeclarativeBase
from typing import List


from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'my.sqlite')


class Base(DeclarativeBase):
    pass


engine = create_engine(connection_string, echo=True)
Session = scoped_session(sessionmaker())


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    date_created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now)

    def __str__(self):
        return f"<User username={self.username}, email={self.email}>"


# remove all tables
Base.metadata.drop_all(engine)

# create all tables
Base.metadata.create_all(engine)
local_session = Session(bind=engine)

user1 = User(username="John", email="john@hua.gr")
local_session.add(user1)
local_session.commit()

# close the connection
local_session.close()
