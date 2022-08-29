from pydantic import BaseModel



class HealthCheck(BaseModel):
    name: str
    version: str
    description: str


class Message(BaseModel):
    message: str
