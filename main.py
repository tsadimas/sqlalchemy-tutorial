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
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    jobs: Mapped[List["Job"]] = relationship(back_populates="user")


    def __str__(self):
        return f"<User username={self.username}, email={self.email}>"

class Job(Base):
    __tablename__ = 'jobs'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="jobs")

    def __str__(self):
        return f"<Job name={self.name}, user = {self.user}"

# remove all tables
Base.metadata.drop_all(engine)

# create all tables
Base.metadata.create_all(engine)
local_session = Session(bind=engine)
user1 = User(username="John", email="john@hua.gr")
job1=Job(name="Programmer", user=user1)
job2=Job(name="Analyst", user=user1)
print(user1.jobs)
for i in user1.jobs:
    print(i)
local_session.add(user1)
local_session.commit()

# remove a job
local_session.delete(job1)
local_session.commit()

#query

users = local_session.query(User).all()
for u in users:
    print(u)
    jobs = local_session.query(Job).filter(Job.user==u).all()
    for j in jobs:
        print(j)

# close the connection
local_session.close()