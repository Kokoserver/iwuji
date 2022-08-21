import typing  as t
from uuid import UUID
from fastapi import HTTPException, status, UploadFile, Request, Response
from app.src.media import models
from app.src.product.models import Product, ProductAttribute, ProductProperty,  Variation
from app.src.category.crud import Category
from app.src.product import schemas
from app.src.media import crud as media_crud
from app.src._base.schemas import Message
from tortoise.models import Q


async def create_product_categories(categories:t.List[str]) -> Message:
    all_categories:t.List[str] = [cat.strip() for cat in categories.split(",")]
    product_cats:t.List[Category] = await Category.filter(name__in=all_categories)
    if product_cats:
        return product_cats
    return []
    
async def delete_product_gallery(productId:UUID) -> Product:
        get_product:Product = await Product.filter(id= productId).prefetch_related("gallery", "pdf_file", "cover_img", "attribute", "property").first()
        if not get_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        check_attribute = await ProductAttribute.filter(id=get_product.attribute.id).first() 

        await media_crud.delete(old_medias=(await get_product.gallery.all() if await get_product.gallery.all() else []))
        await media_crud.delete(old_medias=[(get_product.pdf_file if get_product.pdf_file else [])], is_pdf=True)
        await media_crud.delete(old_medias=[(get_product.cover_img if get_product.cover_img else [])])       
        if check_attribute:
            await check_attribute.delete()
        check_property = await ProductProperty.filter(id=get_product.property.id).first()
        if check_property:
            await check_property.delete()
        await get_product.delete()
        return True




async def create_product(productIn: schemas.ProductIn, cover_img:UploadFile, product_pdf:UploadFile, gallery:t.List[UploadFile], request:Request) -> Message:
    check_product = await Product.filter(name =productIn.name).first()
    if check_product:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
            detail=f"Product already exists, with name {productIn.name}")
    
    pdf_file:t.List[models.Media] = await media_crud.upload(media_objs=[product_pdf],
                                                            request=request,
                                                            is_pdf=True)
    new_product_prop = await ProductProperty.create(**schemas.ProductPropertyIn(**productIn.dict()).dict())
    new_product_attr = await ProductAttribute.create(**schemas.ProductAttributeIn(**productIn.dict()).dict())
    cover_image:t.List[models.Media] = await media_crud.upload(media_objs=[cover_img], request=request)
    new_product = Product(name=productIn.name,
                          description=productIn.description, 
                          attribute=new_product_attr,
                          property=new_product_prop,
                          is_series=productIn.is_series,
                          is_assigned=productIn.is_assigned,
                          is_active=productIn.is_active,
                          pdf_file = (pdf_file[0] if pdf_file else None),
                          cover_img=cover_image[0]
                          )
    new_product.make_slug()
    await new_product.save()
    if productIn.categories:
        product_cats:t.List[Category] = await create_product_categories(productIn.categories) 
        await new_product.categories.add(*product_cats)   
    if gallery is not None:
        gallery_objs:t.List[models.Media] = await media_crud.upload(media_objs=gallery,request=request)
        await new_product.gallery.add(*gallery_objs)
    return Message(message="Product created successfully")

async def get_product(id: UUID) -> Product:
    product:schemas.ProductPydanticOut = await schemas.ProductPydanticOut.from_queryset_single(Product.filter(id=id).first().prefetch_related("gallery", "pdf_file", "cover_img", "attribute", "property"))
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product
        
async def update_product(productId:UUID,
                         productIn: schemas.ProductIn,
                         cover_img:UploadFile,
                         gallery:t.List[UploadFile],
                         request:Request, 
                         product_pdf:UploadFile
                         ) -> Message:
    check_product:Product = await Product.filter(id =productId).select_related("property", "attribute").prefetch_related("gallery").first()
    if not check_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    check_name = await Product.filter(name = productIn.name).first()
    if check_name and check_name.id != productId:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                            detail=f"Product already exists, with name {productIn.name}")

    check_product.name = productIn.name
    check_product.description = productIn.description
    check_product.is_series=productIn.is_series
    check_product.is_assigned=productIn.is_assigned
    check_product.is_active=productIn.is_active
    check_product.make_slug()
    if productIn.categories:
        get_cats = await create_product_categories(productIn.categories)
        if get_cats:
            await  check_product.categories.clear()
            await check_product.categories.add(*get_cats)
    if product_pdf:
        pdf_file:t.List[models.Media] = await media_crud.update(media_objs=[product_pdf],
                                                                old_medias=[check_product.pdf_file],
                                                                request=request,
                                                                is_pdf=True)
        check_product.pdf_file = (pdf_file[0] if pdf_file else None)

    for key, value in schemas.ProductPropertyIn(**productIn.dict()).dict().items():
            setattr(check_product.property, key, value)

    for key, value in schemas.ProductAttributeIn(**productIn.dict()).dict().items():
        if value:
            setattr(check_product.attribute, key, value)

   
    if cover_img:
            new_img = await media_crud.update(media_objs=[cover_img], 
             old_medias=[check_product.cover_img], request=request)
            check_product.cover_img = new_img[0]
            
    if gallery:
        new_media_objs  = await media_crud.update(media_objs=gallery, old_medias=check_product.gallery,request=request)
        if new_media_objs:
            await check_product.gallery.clear()
            await check_product.gallery.add(*new_media_objs)
    await check_product.save()
    return Message(message="Product updated successfully")
    
    
async def get_products(*, limit:int, offset:int, filter:t.Any, is_series:bool, is_assigned:bool, is_active:bool ) -> t.List[Product]:
    return await schemas.ProductPydanticOut.from_queryset(Product.filter(
        Q(name__icontains=filter) | 
        Q(description__icontains=filter)|
        Q(slug__icontains=filter)|
        Q(categories__name__icontains=filter)|
        Q(attribute__language__icontains=filter)
        ).filter(is_series=is_series, is_assigned=is_assigned, is_active=is_active).prefetch_related("property", "attribute", "categories", "gallery", "pdf_file").order_by("-created_at").offset(offset).limit(limit))
    
    
    

async def delete_product(id: UUID) -> Product:
    if (await delete_product_gallery(id)):
       return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error deleting product")
    
    

################# variations ################################

async def create_variation(variation: schemas.VariationIn, 
                          cover_img:UploadFile,
                          request:Request) -> Variation:
    if (await Variation.filter(name = variation.name).first()):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
            detail=f"series with name `{variation.name}` already exists, for product this product")
    new_variation:Variation = Variation(**variation.dict())
    new_variation.make_slug()
    if cover_img:
        new_cover_img = await media_crud.upload(media_objs=[cover_img], request=request)
        new_variation.cover_img = (new_cover_img[0] if new_cover_img else None)
    await new_variation.save()
    return Message(message="series created successfully")


async def get_all_variation(limit:int, offset:int, filter:str = '') -> t.List[Variation]:
    all_variation= await schemas.VariationPydanticOut.from_queryset(Variation.filter(
        Q(name__icontains=filter) | 
        Q(description__icontains=filter)
        ).filter(is_active=True).all().limit(limit).prefetch_related('items').offset(offset))
    return all_variation


async def update_variation(id: UUID, variationIn: schemas.VariationIn, cover_img:UploadFile, request:Request) -> Variation:
    check_variation: Variation = await Variation.filter(id = id).first()
    if not check_variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Series not found")
    if check_variation and check_variation.name == variationIn.name:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
            detail=f"series with name {variationIn.name} already exists")
    check_variation.name = variationIn.name
    check_variation.make_slug()
    check_variation.description = variationIn.description
    if cover_img:
        new_cover_img = await media_crud.update(media_objs=[check_variation.cover_img], 
                                                old_medias=[check_variation.cover_img], request=request)
        check_variation.cover_img = new_cover_img[0]
    await check_variation.save()
    return Message(message="Series updated successfully")

async def get_variation(id: UUID) -> Variation:
    get_variation =  await schemas.VariationPydanticOut.from_queryset_single(Variation.filter(id = id).first())
    if not get_variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variation not found")
    return get_variation


async def delete_variation(id: UUID) -> Variation:
    get_variation:Variation = await Variation.filter(id=id).prefetch_related("cover_img").first()
    if not get_variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variation not found")
    if get_variation.cover_img:
        await media_crud.delete(old_medias=[get_variation.cover_img])
    all_series_product  = await get_variation.items.all()
    if all_series_product:
        for product in all_series_product:
            await delete_product_gallery(product.id)
    await get_variation.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


################# variation product ################################

    
async def add_product_to_variations(dataIn:schemas.VariationProductIn) -> Message:
    product:Product = await Product.filter(id=dataIn.productId).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    if ( await Variation.filter(items__name=product.name).exists()) :
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="book already in variation")
       
    variation:Variation = await Variation.filter(id=dataIn.variationId).first()
    if not variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Variation not found")
    if (await variation.filter(items__name=product.name).exists()):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="book already exists in series")
    product.is_assigned = True
    await product.save()
    await variation.items.add(product)
    return Message(message="book added to series successfully")

async def get_unassigned_products(limit:int, offset:int, filter:str = '') -> t.List[Product]:
    all_products:t.List[Product] = await Product.filter(is_active=True, is_assigned=False, is_series = True).all().limit(limit).offset(offset)
    return all_products

async def get_product_variations(limit:int, offset:int,  seriesId:UUID) -> t.List[Product]:
    all_variation_series:Variation = await Variation.filter(id = seriesId).prefetch_related("items").limit(limit).offset(offset).first()
    if not all_variation_series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Series not found")
    return await all_variation_series.items.all()

async def remove_product_from_variation(dataIn:schemas.VariationProductIn) -> Message:
    product:Product = await Product.filter(id=dataIn.productId).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    variation:Variation = await Variation.filter(id=dataIn.variationId).first()
    if not variation:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Series not found")
    if await variation.items.filter(id=product.id).exists():
        await variation.items.remove(product)
        product.is_assigned = False
        await product.save()
        return Message(message="book removed from series successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found in series")
    





    


