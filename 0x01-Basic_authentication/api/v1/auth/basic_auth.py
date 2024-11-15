#!/usr/bin/python3
from flask import request
import base64
from .auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic"):
            return None
        token  = authorization_header.split(" ") [-1]
        return token