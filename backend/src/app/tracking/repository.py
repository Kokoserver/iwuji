from src.base.repository.base_repository import BaseRepository
from src.app.tracking import model


class Tracking(BaseRepository[model.Tracking]):
    def __init__(self):
        super().__init__(model.Tracking)


tracking_repo = Tracking()
