import typing as t
from fastapi import HTTPException, status, UploadFile, Request, Response
from app.src.media import models
from app.src.product.models import Product, ProductAttribute, ProductProperty, Variation
from app.src.category.crud import Category
from app.src.product import schemas
from app.src.media import crud as media_crud
from app.src._base.schemas import Message
from ormar import or_, and_


async def create_product_categories(categories: t.List[str]) -> Message:
    all_categories: t.List[str] = [cat.strip() for cat in categories.split(",")]
    product_cats: t.List[Category] = await Category.objects.filter(name__in=all_categories).all()
    if product_cats:
        return product_cats
    return []


async def delete_product_gallery(productId: int) -> Product:
    get_product: Product = await Product.objects.select_related(["gallery", "pdf_file", "cover_img", "attribute", "property"]).get_or_none(id=productId)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    check_attribute = await ProductAttribute.objects.get_or_none(id=get_product.attribute.id)

    await media_crud.delete(old_medias=(await get_product.gallery.all() if await get_product.gallery.all() else []))
    await media_crud.delete(old_medias=[(get_product.pdf_file if get_product.pdf_file else [])], is_pdf=True)
    await media_crud.delete(old_medias=[(get_product.cover_img if get_product.cover_img else [])])
    if check_attribute:
        await check_attribute.delete()
    check_property = await ProductProperty.objects.get_or_none(id=get_product.property.id)
    if check_property:
        await check_property.delete()
    await get_product.delete()
    return True


async def create_product(productIn: schemas.ProductIn, cover_img: UploadFile, product_pdf: UploadFile, gallery: t.List[UploadFile], request: Request) -> Message:
    check_product = await Product.objects.get_or_none(name=productIn.name)
    if check_product:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Product already exists, with name {productIn.name}")

    pdf_file: t.List[models.Media] = await media_crud.upload(media_objs=[product_pdf],
                                                             request=request,
                                                             is_pdf=True)
    new_product_prop = await ProductProperty.objects.create(**schemas.ProductPropertyIn(**productIn.dict()).dict())
    new_product_attr = await ProductAttribute.objects.create(**schemas.ProductAttributeIn(**productIn.dict()).dict())
    cover_image: t.List[models.Media] = await media_crud.upload(media_objs=[cover_img], request=request)
    new_product: Product = Product(name=productIn.name,
                                   description=productIn.description,
                                   attribute=new_product_attr,
                                   property=new_product_prop,
                                   is_series=productIn.is_series,
                                   is_assigned=productIn.is_assigned,
                                   is_active=productIn.is_active,
                                   pdf_file=(pdf_file[0] if pdf_file else None),
                                   cover_img=cover_image[0]
                                   )
    await new_product.save()
    if productIn.categories:
        product_cats: t.List[Category] = await create_product_categories(productIn.categories)
        [await new_product.categories.add(product_cat) for product_cat in product_cats if product_cats]
    if gallery is not None:
        gallery_objs: t.List[models.Media] = await media_crud.upload(media_objs=gallery, request=request)
        [await new_product.gallery.add(gallery_obj) for gallery_obj in gallery_objs if gallery_obj]
    return Message(message="Product created successfully")


async def get_product(id: int) -> Product:
    product = await Product.objects.select_related(["gallery", "pdf_file", "cover_img", "attribute", "property"]).get_or_none(id=id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    return product


async def update_product(productId: int,
                         productIn: schemas.ProductIn,
                         cover_img: UploadFile,
                         gallery: t.List[UploadFile],
                         request: Request,
                         product_pdf: UploadFile
                         ) -> Message:
    check_product: Product = await Product.objects.select_related(["property", "attribute", "gallery"]).get_or_none(id=productId)
    if not check_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    check_name = await Product.objects.get_or_none(name=productIn.name)
    if check_name and check_name.id != productId:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Product already exists, with name {productIn.name}")

    await check_product.update(name=productIn.name,
                               description=productIn.description,
                               is_series=productIn.is_series,
                               is_assigned=productIn.is_assigned,
                               is_active=productIn.is_active
                               )
    if productIn.categories:
        get_cats = await create_product_categories(productIn.categories)
        if get_cats:
            await check_product.categories.clear()
            [await check_product.categories.add(cat) for cat in get_cats if cat]
    if product_pdf:
        pdf_file: t.List[models.Media] = await media_crud.update(media_objs=[product_pdf],
                                                                 old_medias=[
                                                                     check_product.pdf_file],
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
        check_product.cover_img = (new_img[0] if new_img else None)

    if gallery:
        new_media_objs = await media_crud.update(media_objs=gallery, old_medias=check_product.gallery, request=request)
        if len(new_media_objs) > 0:
            await check_product.gallery.clear()
            [await check_product.gallery.add(new_media_obj) for new_media_obj in new_media_objs if new_media_obj]

    return Message(message="Product updated successfully")


async def get_products(*, limit: int, offset: int, filter: str, is_series: bool, is_assigned: bool, is_active: bool) -> t.List[Product]:
    return await Product.objects.filter(
        and_(is_active=is_active)).filter(
        and_(is_series=is_series)
    ).filter(is_assigned=is_assigned).filter(
        or_(name__icontains=filter,
            description__icontains=filter,
            slug__icontains=filter,
            categories__name__icontains=filter,
            attribute__language__icontains=filter)
    ).select_related(["property", "cover_img", "attribute", "categories", "gallery", "pdf_file"]
                     ).order_by("-created_at").offset(offset).limit(limit).all()


async def delete_product(id: int) -> Product:
    if (await delete_product_gallery(id)):
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="error deleting product")


################# variations ################################

async def create_variation(variation: schemas.VariationIn,
                           cover_img: UploadFile,
                           request: Request) -> Variation:
    if (await Variation.objects.get_or_none(name=variation.name)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"series with name `{variation.name}` already exists, for product this product")
    new_variation: Variation = Variation(**variation.dict())
    if cover_img:
        new_cover_img = await media_crud.upload(media_objs=[cover_img], request=request)
        new_variation.cover_img = (new_cover_img[0] if new_cover_img else None)
    await new_variation.save()
    return Message(message="series created successfully")


async def get_all_variation(is_active: bool, limit: int, offset: int, filter: str = '') -> t.List[Variation]:
    all_variation = await Variation.objects.select_related(
        [Variation.cover_img, 'items__property', "items__attribute", "items__cover_img"]
    ).filter(and_(is_active=is_active)).filter(
        or_(name__icontains=filter, description__icontains=filter)
    ).limit(limit).offset(offset).all()
    return all_variation


async def update_variation(id: int, variationIn: schemas.VariationIn, cover_img: UploadFile, request: Request) -> Variation:
    check_variation: Variation = await Variation.objects.get_or_none(id=id)
    if not check_variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Series not found")
    if check_variation and check_variation.name == variationIn.name and check_variation.id != id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"series with name {variationIn.name} already exists")
    await check_variation.update(
        name=variationIn.name,
        description=variationIn.description,
        is_active=variationIn.is_active
    )
    if cover_img:
        new_cover_img = await media_crud.update(media_objs=[cover_img],
                                                old_medias=[check_variation.cover_img],
                                                request=request)
        await check_variation.update(cover_img=(new_cover_img[0] if new_cover_img else None))
    return Message(message="Series updated successfully")


async def get_variation(id: int) -> Variation:
    get_variation = await Variation.objects.select_related(
        [Variation.cover_img, 'items__property', "items__attribute", "items__cover_img"]
    ).get_or_none(id=id)
    if not get_variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Variation not found")
    return get_variation


async def delete_variation(id: int) -> Variation:
    get_variation: Variation = await Variation.objects.select_related(["cover_img"]).get_or_none(id=id)
    if not get_variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Variation not found")
    if get_variation.cover_img:
        await media_crud.delete(old_medias=[get_variation.cover_img])
    if get_variation.items:
        for product in get_variation.items:
            await delete_product_gallery(product.id)
    await get_variation.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


################# variation product ################################


async def add_product_to_variations(dataIn: schemas.VariationProductIn) -> Message:
    product: Product = await Product.objects.get_or_none(id=dataIn.productId)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    if (await Variation.objects.filter(items__name=product.name).exists()) :
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="book already in variation")

    variation: Variation = await Variation.objects.get_or_none(id=dataIn.variationId)
    if not variation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Variation not found")
    if (await Variation.objects.filter(items__name=product.name, id=dataIn.productId).exists()):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="book already exists in series")
    await product.update(is_assigned=True)
    await variation.items.add(product)
    return Message(message="book added to series successfully")


async def get_product_variations(seriesId: int) -> t.List[Product]:
    all_variation_series: Variation = await Variation.objects.select_related(
        [Variation.cover_img, 'items__property', "items__attribute", "items__cover_img"]
    ).get_or_none(id=seriesId)
    if not all_variation_series:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Series not found")
    return all_variation_series.items


async def remove_product_from_variation(dataIn: schemas.VariationProductIn) -> Message:
    product: Product = await Product.objects.get_or_none(id=dataIn.productId)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found")
    if not (await Variation.objects.filter(id=dataIn.variationId).exists()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Series not found")
    get_product_in_var = await Variation.objects.select_related("items").get_or_none(items__id=product.id, id=dataIn.variationId)
    if get_product_in_var:
        await get_product_in_var.items.remove(product)
        await product.update(is_assigned=False)
        return Message(message="book removed from series successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="book not found in series")
