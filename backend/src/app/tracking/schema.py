import datetime
import typing as t
import uuid
import pydantic as pyd


class ITrackIn(pyd.BaseModel):
    item_tracking_id: str = pyd.Field(..., description="tracking ID")
    location: str = pyd.Field(..., description="Location")


class ITrackOut(pyd.BaseModel):
    id: uuid.UUID
    item_id: uuid.UUID
    location: str


class ITrackUpdateIn(pyd.BaseModel):
    location: str = pyd.Field(..., description="Location")
