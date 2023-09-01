#!/usr/bin/env python3
"""Module for bcrypt"""
import bcrypt


def hash_password(password: str) -> bcrypt.hashpw:
    """Return a salted hashed password

    Args:
        password(str): password
    """
    salted = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salted)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Returns a boolean"""
    if not bcrypt.checkpw(password.encode("utf-8"), hash_password(password)):
        return False
    return True
