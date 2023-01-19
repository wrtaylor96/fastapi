# -*- coding: utf-8 -*-
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Application"
    REQUES_URI: str = "https://reqres.in/api"


settings = Settings()
