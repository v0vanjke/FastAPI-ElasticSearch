from pydantic import BaseModel
import datetime
from typing import List

class BaseClass(BaseModel):
    class Config:

        orm_mode = True
        from_attributes = True


class ShowRubric(BaseClass):
    id: int
    title: str


class ShowPost(BaseClass):
    id: int
    text: str
    created_date: datetime.datetime
    rubrics: List[ShowRubric] = []


class PostCreate(BaseClass):
    text: str
    rubrics: List[int] = []


class RubricCreate(BaseClass):
    title: str
