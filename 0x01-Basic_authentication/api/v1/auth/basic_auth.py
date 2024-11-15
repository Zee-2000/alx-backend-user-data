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
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64encode(decoded)
            return decoded.decode('utf-8')
        except Exception:
            return None