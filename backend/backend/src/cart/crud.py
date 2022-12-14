from fastapi import status, HTTPException, Response

from backend.src.cart import schemas
from backend.src.cart.models import Cart
from backend.src.user.models import User
from backend.src.product.models import Product, ProductProperty


async def check_product_in_quantity(productId: int, cart: schemas.CartIn) -> Product:
    get_product: Product = await Product.objects.select_related(['property']).get_or_none(id=productId)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='book does not exist')
    product_prop: ProductProperty = get_product.property
    if not product_prop.paper_back_qty >= cart.paper_back_qty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Hard back book quantity is less than cart quantity, `{product_prop.paper_back_qty}`')
    if not product_prop.hard_back_qty >= cart.hard_back_qty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Hard back book quantity is less than cart quantity, `{product_prop.hard_back_qty}`')
    return get_product


async def create_cart(cart: schemas.CartIn, user: User):
    get_product = await check_product_in_quantity(cart.productId, cart)
    add_cart = await Cart.objects.create(
        pdf=cart.pdf,
        paper_back_qty=cart.paper_back_qty,
        hard_back_qty=cart.hard_back_qty,
        user=user,
        product=get_product)
    if add_cart:
        new_cart = await get_cart(add_cart.id, user)
        return new_cart
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='product does not exist in cart')


async def update_cart(cart: schemas.CartUpdateIn, user: User):
    get_cart_product = await Cart.objects.select_related(["product__property",
                                                          "product__cover_img"]).filter(id=cart.cartId,
                                                                                        user=user).first()
    if not get_cart_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='product does not exist in cart')
    await check_product_in_quantity(get_cart_product.product.id, cart)
    for key, value in cart.dict(exclude={'cartId'}).items():
        setattr(get_cart_product, key, value)
    await get_cart_product.upsert()
    return get_cart_product


async def get_all_cart(user: User):
    data = await Cart.objects.select_related(["product__property", "product__cover_img"]).filter(user=user).all()
    return data


async def get_cart(cartId: int, user: User):
    data = await Cart.objects.select_related(["product__property",
                                              "product__cover_img"]).filter(id=cartId, user=user).first()
    return data


async def delete_cart(cartId: int, user: User):
    get_cart = await Cart.objects.get_or_none(id=cartId, user=user)
    if not get_cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='product does not exist in cart')
    await get_cart.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
