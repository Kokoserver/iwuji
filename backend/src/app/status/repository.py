from src.base.repository.base_repository import BaseRepository
from src.app.status import model


class StatusRepository(BaseRepository[model.Status]):
    def __init__(self):
        super().__init__(model.Status)


status_repo = StatusRepository()
