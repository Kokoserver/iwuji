import typing as t
from app.database.document import BaseMeta, DateMixin, Model, fields as f


class Permission(Model, DateMixin):
    class Meta(BaseMeta):
       tablename: str = "iw_permission"
    name:str = f.String(max_length=50, nullable=True)




    
