from src.base.repository.base_repository import BaseRepository
from src.app.author import model


class AuthorRepository(BaseRepository[model.Author,]):
    def __init__(self):
        super().__init__(model.Author)


author_repo = AuthorRepository()
