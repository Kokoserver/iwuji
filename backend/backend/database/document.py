import datetime
import ormar
from ormar import fields
from backend.database import conf


class BaseMeta(ormar.ModelMeta):
    database = conf.database
    metadata = conf.metadata


class Model(ormar.Model):
    class Meta(BaseMeta):
        abstract = True

    id: int = fields.Integer(autoincrement=True, primary_key=True)


class DateMixin:
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    updated_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
