__author__ = 'id301'

from pydantic import BaseModel


class JsTestTask(BaseModel):
    """Модельный класс JsTestTask"""
    name: str
    image: str
    price: int