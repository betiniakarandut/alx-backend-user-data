#!/usr/bin/env python3
"""Module to create a SQLAlchemy model named User"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer)

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    """Create users table"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)

    def __init__(self, email, hashed_password, session_id, reset_token):
        """Create instance of User object"""
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

    def __repr__(self):
        """Prints official representation of users class"""
        return"<User(email='%s', session_id='%s',)>" % (
                     self.email, self.session_id,)
