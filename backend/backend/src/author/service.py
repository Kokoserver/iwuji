import typing

from backend.src.author.models import Author
from backend.src._base.service import BaseService


class AddressService:
    model = Author
    base_services = BaseService

    @staticmethod
    async def get(*args, **kwargs):
        return await AddressService.base_services.get(*args, **kwargs)

    @staticmethod
    async def get_or_create(*args, **kwargs) -> model:
        return await AddressService.base_services.get_or_create(*args, **kwargs)

    @staticmethod
    def get_list(*args, **kwargs) -> typing.List[model]:
        pass

    @staticmethod
    async def update(*args, **kwargs) -> model:
        return await AddressService.base_services.update(*args, **kwargs)

    @staticmethod
    async def update_or_create(*args, **kwargs) -> model:
        return await AddressService.base_services.update_or_create(*args, **kwargs)

    @staticmethod
    async def delete(*args, **kwargs) -> model:
        return await AddressService.base_services.remove(*args, **kwargs)
