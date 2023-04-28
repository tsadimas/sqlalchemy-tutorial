from __future__ import annotations
from sqlalchemy import String, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, Mapped, mapped_column, relationship, DeclarativeBase
from typing import List
from datetime import datetime


class Base(DeclarativeBase):
    pass




class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    date_created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now)
    jobs: Mapped[List["Job"]] = relationship(back_populates="user")

    def __str__(self):
        return f"<User username={self.username}, email={self.email}>"


class Job(Base):
    __tablename__ = 'jobs'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="jobs")

    def __str__(self):
        return f"<Job name={self.name}, user = {self.user}"