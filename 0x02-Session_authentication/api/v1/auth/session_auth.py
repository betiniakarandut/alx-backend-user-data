#!/usr/bin/env python3
"""Authentication mechanism for the API
"""
from os import getenv
import os

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Authentication mechanism class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id


if os.getenv("USE_SESSION_AUTH") == "1":
    auth = Session_Auth()
else:
    auth = Auth()
