from src.base.repository.base_repository import BaseRepository
from src.app.category import model


class CategoryRepository(BaseRepository[model.Category]):
    def __init__(self):
        super().__init__(model.Category)
        
    


category_repo = CategoryRepository()
