import datetime
from typing import List, Optional
from pydantic import BaseModel


class Sound(BaseModel):
    name: str


class Dog(BaseModel):
    birthday: datetime
    weight: float = Optional[None]
    sound: List[Sound] = []


dogs = Dog(birthday=datetime.datetime.now(),
           weight=12.3,
           sound=[Sound(name="wangwang")])

print(dogs.json())
print(dogs.dict())
