from src.base.repository.base_repository import BaseRepository
from src.app.user_title import model


class UserTitleRepository(BaseRepository[model.UserTitle]):
    def __init__(self):
        super().__init__(model.UserTitle)


user_title_repo = UserTitleRepository()
