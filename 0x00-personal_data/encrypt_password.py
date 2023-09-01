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
