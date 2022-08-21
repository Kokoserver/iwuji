
from uuid import UUID
from fastapi import  status, HTTPException, Response
from app.src._base.schemas import Message
from app.src.cart import  schemas
from app.src.cart.models import Cart
from app.src.user.models import User
from app.src.product.models import Product, ProductAttribute


async def check_product_in_quantity(productId:UUID, cart:schemas.CartIn) -> Cart:
    get_product:Product = await Product.filter(id=productId).prefetch_related('attribute').first()
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product does not exist')
    product_att:ProductAttribute = get_product.attribute
    if not product_att.paper_back_qty >= cart.paper_back_qty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Hard back book quantity is less than cart quantity, f{product_att.paper_back_qty}')
    if  product_att.hard_back_qty >= cart.hard_back_qty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Hard back book quantity is less than cart quantity, f{product_att.hard_back_qty}')
    return Message(message='Product is available in cart')


async def create_cart(cart:schemas.CartIn, user:User ):
    get_product = await check_product_in_quantity(cart.productId, cart)
    add_cart = await Cart.create(**cart.dict(exclude=['productId']), user=user, product=get_product)
    return add_cart
    


async def update_cart(id:UUID, cart:schemas.CartIn, user:User):
    await check_product_in_quantity(cart.productId, cart)
    get_cart_product = await Cart.filter(id=id, user=user).first()
    if not get_cart_product:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product does not exist in cart')
    for key, value in cart.dict(exclude=['productId']).items():
        setattr(get_cart_product, key, value)
    await get_cart_product.save()
    return get_cart_product

async def get_all_cart(user:User):
    return await Cart.filter(user=user).prefetch_related('product').all()

async def delete_cart(id:UUID, user:User):
    get_cart = await Cart.filter(id=id, user=user).first()
    if not get_cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product does not exist in cart')
    await get_cart.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
