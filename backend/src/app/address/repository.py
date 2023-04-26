from src.base.repository.base_repository import BaseRepository
from src.app.address import model


class AddressRepository(BaseRepository[model.Address]):
    def __init__(self):
        super().__init__(model.Address)


address_repo = AddressRepository()
