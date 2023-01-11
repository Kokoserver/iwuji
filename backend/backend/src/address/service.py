import typing

from backend.src.address.models import ShippingAddress
from backend.src._base.service import BaseService


class AddressService:
    model = ShippingAddress
    base_services = BaseService

    @staticmethod
    async def get(*args, **kwargs):
        return await AddressService.base_services.get(*args, **kwargs)

    @staticmethod
    async def get_or_create(*args, **kwargs) -> ShippingAddress:
        return await AddressService.base_services.get_or_create(*args, **kwargs)

    @staticmethod
    def get_list(*args, **kwargs) -> typing.List[ShippingAddress]:
        pass

    @staticmethod
    async def update(*args, **kwargs) -> ShippingAddress:
        return await AddressService.base_services.update(*args, **kwargs)

    @staticmethod
    async def update_or_create(*args, **kwargs) -> ShippingAddress:
        return await AddressService.base_services.update_or_create(*args, **kwargs)

    @staticmethod
    async def delete(*args, **kwargs) -> ShippingAddress:
        return await AddressService.base_services.remove(*args, **kwargs)
