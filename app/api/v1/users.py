# -*- coding: utf-8 -*-
from typing import Any
import requests

from fastapi import APIRouter

from app.core import settings
from app.models.v1.user import User


router = APIRouter()


@router.get("/{user_id}")
def get_users(user_id: int) -> User:
    """
    Retrieve user by id.

    """
    response: requests.Response = requests.get(f"{settings.REQUES_URI}/users/{user_id}")
    data: Any = response.json()["data"]

    return User(
        id=data["id"],
        email=data["email"],
        first_name=data["first_name"],
        last_name=data["last_name"],
        avatar=data["avatar"],
    )
