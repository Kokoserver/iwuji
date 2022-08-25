from fastapi import  status, HTTPException, Response
from app.src._base.schemas import Message
from app.src.cart import  schemas
from app.src.cart.models import Cart
from app.src.user.models import User
from app.src.product.models import Product, ProductProperty


async def check_product_in_quantity(productId:int, cart:schemas.CartIn) -> Cart:
    get_product:Product = await Product.objects.select_related(['property']).get_or_none(id=productId)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='book does not exist')
    product_prop:ProductProperty = get_product.property
    if not product_prop.paper_back_qty >= cart.paper_back_qty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Hard back book quantity is less than cart quantity, `{product_prop.paper_back_qty}`')
    if not product_prop.hard_back_qty >= cart.hard_back_qty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Hard back book quantity is less than cart quantity, `{product_prop.hard_back_qty}`')
    return get_product


async def create_cart(cart:schemas.CartIn, user:User ):
    get_product = await check_product_in_quantity(cart.productId, cart)
    add_cart = await Cart.objects.create(
        pdf = cart.pdf,
        paper_back_qty = cart.paper_back_qty,
        hard_back_qty = cart.hard_back_qty,
        user=user, 
        product=get_product)
    if  add_cart:
       return Message(message='Cart created successfully')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product does not exist in cart')
    


async def update_cart(id:int, cart:schemas.CartIn, user:User):
    await check_product_in_quantity(cart.productId, cart)
    get_cart_product = await Cart.objects.filter(id=id, user=user).first()
    if not get_cart_product:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product does not exist in cart')
    for key, value in cart.dict(exclude=['productId']).items():
        setattr(get_cart_product, key, value)
    await get_cart_product.save()
    return get_cart_product

async def get_all_cart(user:User):
    data = await Cart.objects.filter(user=user).select_related(['product']).all()
    return data
    

async def delete_cart(id:int, user:User):
    get_cart = await Cart.objects.get_or_none(id=id, user=user)
    if not get_cart:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='product does not exist in cart')
    await get_cart.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
