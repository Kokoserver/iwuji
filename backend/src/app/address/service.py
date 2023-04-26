import uuid
import typing as t
from fastapi import status, Response
from src.app.user.model import User
from src.lib.errors import error
from src.app.address import schema, model
from src.app.address.repository import address_repo


async def create(
    data_in: schema.IAddressIn,
    user: User,
) -> model.Address:
    check_address = await address_repo.get_by_attr(
        attr=dict(**data_in.dict(), user=user), first=True
    )

    if check_address:
        raise error.DuplicateError("address already exists")
    new_address = await address_repo.create(dict(**data_in.dict(), user=user))
    return new_address


async def get(
    address_id: uuid.UUID,
    user: User,
) -> model.Address:
    get_address = await address_repo.get_by_attr(attr=dict(id=address_id, user=user), first=True)
    if not get_address:
        raise error.NotFoundError("Address not found")
    return get_address


async def update(
    address_id: uuid.UUID,
    data_in: schema.IAddressIn,
    user: User,
) -> model.Address:
    check_if_exist = await address_repo.get_by_attr(
        attr=dict(
            id=address_id,
            user=user,
            **{k: v for k, v in data_in.dict(exclude_defaults=True).items() if v is not None},
        ),
        first=True,
    )
    if check_if_exist is not None:
        raise error.DuplicateError("address already exists")
    get_address = await address_repo.get_by_attr(attr=dict(id=address_id, user=user), first=True)
    if not get_address:
        raise error.NotFoundError("Address not found")
    result = await address_repo.update(id=address_id, obj=data_in)
    return result


async def filter(
    user: User,
    filter: str = "",
    per_page: int = 10,
    page: int = 0,
    select: str = "",
) -> t.List[model.Address]:
    get_address = await address_repo.filter(
        filter_string=filter,
        per_page=per_page,
        page=page,
        select_columns=select,
        strict_search=dict(user=user),
    )
    return get_address


async def get_total_count(user: User) -> dict:
    total_add = await address_repo.get_by_attr(attr=dict(user=user))
    return dict(total=len(total_add))


async def delete(
    address_id: uuid.UUID,
    user: User,
) -> Response:
    get_address = await address_repo.get_by_attr(attr=dict(id=address_id, user=user), first=True)

    if not get_address:
        raise error.NotFoundError("Address not found")
    await address_repo.delete(address_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
