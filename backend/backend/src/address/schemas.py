import pydantic


class AddressIn(pydantic.BaseModel):
    street: str = pydantic.Field(max_length=50)
    state: str = pydantic.Field(max_length=20)
    city: str = pydantic.Field(max_length=20)
    country: str = pydantic.Field(max_length=20)
    tel: str = pydantic.Field(max_length=15)
    zipcode: str = pydantic.Field(max_length=10)


class AddressOut(AddressIn):
    id: int
