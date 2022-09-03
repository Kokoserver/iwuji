from typing import List
from fastapi import HTTPException, status, Response
from app.src.address.models import ShippingAddress
from app.src.address import schemas
from app.src._base.schemas import Message
from ..user.models import User


async def create_address(address: schemas.AddressIn, user: User) -> ShippingAddress:
    (address_obj, created) = await ShippingAddress.objects.get_or_create(**address.dict(), user=user)
    if created:
        return address_obj
    raise HTTPException(status_code=400, detail='Address already exists')


async def update_address(addressId: int, address: schemas.AddressIn, user: User) -> Message:
    get_address = await ShippingAddress.objects.get_or_none(id=addressId, user=user)
    if not get_address:
        raise HTTPException(status_code=404, detail='Address does not exist')
    if get_address.street == address.street and get_address.city == address.city and get_address.state == address.state :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Address already exists')
    for key, value in address.dict().items():
        setattr(get_address, key, value)
    await get_address.upsert()
    return Message(message='Address updated successfully')


async def delete_address(addressId: int, user: User) -> None:
    get_address = await ShippingAddress.objects.get_or_none(id=addressId, user=user)
    if not get_address:
        raise HTTPException(status_code=404, detail='Address does not exist')
    await get_address.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def get_address(addressId: int, user: User) -> ShippingAddress:
    get_add = await ShippingAddress.objects.get_or_none(id=addressId, user=user)
    if not get_add:
        raise HTTPException(status_code=404, detail='Address does not exist')
    return get_add


async def get_all_address(user: User) -> List[ShippingAddress]:
    all_add: ShippingAddress = await ShippingAddress.objects.filter(user=user).all()
    return all_add