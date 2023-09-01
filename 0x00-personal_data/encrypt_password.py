#!/usr/bin/env python3
"""Module for bcrypt"""
import bcrypt


def hash_password(password: str) -> bcrypt.hashpw:
    """Return a salted hashed password
    """
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd


password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))
