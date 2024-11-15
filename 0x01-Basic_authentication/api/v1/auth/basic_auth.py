#!/usr/bin/python3
from flask import request
import base64
from .auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    pass    