import typing as t
from backend.database.document import BaseMeta, DateMixin, Model, fields as f


class Permission(Model, DateMixin):
    class Meta(BaseMeta):
        tablename: str = "iw_permission"

    name: str = f.String(max_length=50, nullable=True)
