from typing import List 
from fastapi import APIRouter, status, Depends, File, UploadFile, Request
from app.src._base.schemas import Message
from app.src.product import crud, schemas

product = APIRouter()

@product.post("/",   status_code=status.HTTP_201_CREATED)
async def create_product(
    request:Request,
    cover_img:UploadFile = File(...),
    gallery:List[UploadFile] = File(None),
    pdf_file:UploadFile = File(...),
    product: schemas.ProductIn = Depends(schemas.ProductIn.as_form),
    ):
    return await crud.create_product(
        productIn=product, 
        cover_img=cover_img, 
        gallery=gallery, 
        product_pdf=pdf_file, 
        request=request
        )
    
@product.get("/{productId}", status_code=status.HTTP_200_OK, response_model=schemas.ProductOut)
async def get_product(productId:int):
    return await crud.get_product(id=productId)
    
@product.put("/{productId}",   status_code=status.HTTP_201_CREATED)
async def update_product(
    productId:int,
    request:Request,
    pdf_file:UploadFile = File(None),
    cover_img:UploadFile = File(None),
    gallery:List[UploadFile] = File(None),
    product: schemas.ProductIn = Depends(schemas.ProductIn.as_form),):
    return await crud.update_product(
        productId=productId,
        productIn=product, 
        product_pdf=pdf_file,
        cover_img=cover_img,
        gallery=gallery,
        request=request
        )
    
@product.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ProductOut])
async def get_all_products(limit:int = 10, offset:int = 0, filter:str = '', is_series:bool = False, is_assigned:bool = False, is_active:bool = True) -> List[schemas.ProductOut]:
    return await crud.get_products(limit=limit, offset=offset, filter=filter, is_series=is_series, is_assigned=is_assigned, is_active=is_active)




@product.delete("/{productId}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(productId:int) -> None:
    return await crud.delete_product(id=productId)


########### Variation #############

variation = APIRouter()

@variation.post("/", status_code=status.HTTP_201_CREATED)
async def create_product_variation(request:Request, 
                                   cover_img:UploadFile = File(...),
                                   variation: schemas.VariationIn=Depends(
                                    schemas.VariationIn.as_form)) -> schemas.VariationOut:
    return await crud.create_variation(cover_img=cover_img, 
                                       variation=variation, 
                                       request=request
                                       )


@variation.put("/", status_code=status.HTTP_200_OK)
async def add_product_to_variation(dataIn:schemas.VariationProductIn) -> Message:
    return await crud.add_product_to_variations(dataIn)

@variation.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.VariationOut])
async def get_all_variations(limit:int = 10, offset:int = 0, filter:str = '', is_active:bool=True) -> List[schemas.VariationOut]:
    return await crud.get_all_variation(limit=limit, offset=offset, filter=filter, is_active=is_active)

@variation.put("/{variationId}", status_code=status.HTTP_200_OK)
async def update_product_variation(variationId:int, request:Request, cover_img:UploadFile = File(None), variation: schemas.VariationIn=Depends(schemas.VariationIn.as_form)) -> schemas.VariationOut:
    return await crud.update_variation(id=variationId, cover_img=cover_img, variationIn=variation, request=request)

@variation.get("/{variationId}/products", status_code=status.HTTP_200_OK, response_model=List[schemas.ProductOut])
async def get_product_variations(variationId:int) -> List[schemas.VariationOut]:
    return await crud.get_product_variations( seriesId=variationId)

@variation.patch("/", status_code=status.HTTP_200_OK)
async def remove_product_from_variation(dataIn:schemas.VariationProductIn) -> Message:
    return await crud.remove_product_from_variation(dataIn)


@variation.get("/{variationId}", status_code=status.HTTP_200_OK, response_model=schemas.VariationOut)
async def get_variation(variationId:int) -> schemas.VariationOut:
    return await crud.get_variation(id=variationId)


@variation.delete("/{variationId}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_variation(variationId:int) -> None:
    return await crud.delete_variation(id=variationId)