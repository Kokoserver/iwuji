from typing import List
from fastapi import HTTPException, status, Response


from backend.src.address.models import ShippingAddress
from backend.src.address import schemas
from backend.src._base.schemas import Message
from ..user.models import User
from backend.src.order.models import Order


async def create_address(address: schemas.AddressIn, user: User) -> ShippingAddress:
    (address_obj, created) = await ShippingAddress.objects.get_or_create(**address.dict(), user=user)
    if created:
        return address_obj
    raise HTTPException(status_code=400, detail='Address already exists')


async def update_address(addressId: int, address: schemas.AddressIn, user: User) -> Message:
    user_address = await ShippingAddress.objects.get_or_none(id=addressId, user=user)
    if not user_address:
        raise HTTPException(status_code=404, detail='Address does not exist')
    if user_address.street == address.street and \
            user_address.city == address.city and user_address.state == address.state:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Address already exists')
    for key, value in address.dict().items():
        setattr(user_address, key, value)
    await user_address.upsert()
    return Message(message='Address updated successfully')


async def delete_address(addressId: int, user: User) -> Response:
    user_address = await ShippingAddress.objects.get_or_none(id=addressId, user=user)
    check_address_in_order = await Order.objects.filter(shipping_address=user_address).exists()
    if check_address_in_order:
        raise HTTPException(status_code=400, detail='address already in order')
    if not user_address:
        raise HTTPException(status_code=404, detail='Address does not exist')
    await user_address.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


async def get_address(addressId: int, user: User) -> ShippingAddress:
    get_add = await ShippingAddress.objects.get_or_none(id=addressId, user=user)
    if not get_add:
        raise HTTPException(status_code=404, detail='Address does not exist')
    return get_add


async def get_all_address(user: User) -> List[ShippingAddress]:
    all_add: List[ShippingAddress] = await ShippingAddress.objects.filter(user=user).all()
    return all_add
