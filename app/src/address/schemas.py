from uuid import UUID
from pydantic import BaseModel, Field

class AddressIn(BaseModel):
    street:str = Field(max_length=20)
    state:str = Field(max_length=20)
    city :str = Field(max_length=20)
    country:str = Field(max_length=20)
    tel:str = Field(max_length=15)
    zipcode:str = Field(max_length=10)
    
class AddressOut(AddressIn):
    id:UUID