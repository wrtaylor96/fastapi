# -*- coding: utf-8 -*-
from unittest.mock import patch

from app.api.v1.users import get_users
from app.models.v1.user import User


@patch("app.api.v1.users.requests.get")
def test_get_users(mock_get):
    mock_response = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg",
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
        },
    }
    mock_get.return_value.json.return_value = mock_response

    assert get_users(2) == User(
        id=2,
        email="janet.weaver@reqres.in",
        first_name="Janet",
        last_name="Weaver",
        avatar="https://reqres.in/img/faces/2-image.jpg",
    )
