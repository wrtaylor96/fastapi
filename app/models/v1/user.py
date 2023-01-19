# -*- coding: utf-8 -*-
from pydantic import BaseModel

"""
REQUES User model

"""


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
