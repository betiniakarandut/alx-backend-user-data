#!/usr/bin/env python3
"""Authentication mechanism for the API
"""
from os import getenv
import os


from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Authentication mechanism class"""
    pass


if os.getenv("USE_SESSION_AUTH") == "1":
    auth = Session_Auth()
else:
    auth = Auth()
