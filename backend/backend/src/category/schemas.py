import pydantic


class CategoryIn(pydantic.BaseModel):
    name: str


class CategoryOut(pydantic.BaseModel):
    id: int
    name: str
