import typing as t
from sqlalchemy import select
from src.base.repository.base_repository import BaseRepository
from src.app.permission import model


class PermissionRepository(BaseRepository[model.Permission,]):
    def __init__(self):
        super().__init__(model.Permission)

    async def get_by_names(self, names: t.List[str]) -> t.List[model.Permission]:
        stm = select(self.model).where(self.model.name.in_(names))
        get_cats = await self.db.execute(stm)
        return get_cats.scalars().all()


permission_repo = PermissionRepository()
