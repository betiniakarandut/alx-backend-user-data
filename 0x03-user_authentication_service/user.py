#!/usr/bin/env python3
"""Module to create a SQLAlchemy model named User"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine,
                        Column,
                        Sequence,
                        String,
                        Integer)

engine = create_engine('sqlite:///:memory:', echo=True)
Base = sqlalchemy.orm.declarative_base()
Column(Integer, Sequence('users_id_seq'), primary_key=True)


class User(Base):
    """Create users table"""
    __tablename__ = 'users'

    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __init__(self, email, hashed_password, session_id, reset_token):
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

    def __repr__():
        """Prints official representation of users class"""
        return"<User(email='%s'," +\
              "hashed_password='%s'," +\
              "session_id='%s'," +\
              "reset_token='%s')>" % (
                self.email,
                self.hashed_password,
                self.session_id,
                self.reset_token)
