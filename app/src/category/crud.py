from typing import List
from fastapi import status, Response, HTTPException
from uuid import UUID
from app.src._base.schemas import Message
from app.src.category.models import Category
from app.src.category import schemas

async def create_category(new_data:schemas.CategoryIn)->Message:
   _, created = await Category.get_or_create(name=new_data.name)
   if  not created:
       raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                           detail="Category already exists")
   return Message(message="Category created successfully")

async def get_category(id:UUID)->Category:
    check_category = await Category.filter(id=id).first()
    if check_category:
        return check_category
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Category not found")
    

async def get_all_categories(limit:int = 10, offset:int = 0, filter:str = '')->List[Category]:
   return await Category.filter(name__icontains=filter).offset(offset).limit(limit)
       

async def update_category(id:UUID, new_data:schemas.CategoryIn)->Category:
    check_category = await Category.filter(id=id).first()
    if not check_category:
       raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND, 
           detail="Category not found")
    if await Category.filter(name=new_data.name).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Category already exists")
    for key, value in new_data.dict().items():
        if value != None:
           setattr(check_category, key, value)
    await check_category.save()
    return Message(message="Category updated successfully")
    

async def delete_category(id:UUID)->None:
    check_category = await Category.filter(pk=id).first()
    if not check_category:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    await check_category.delete()
    return Response(status_code=status.HTTP_204_NO_CONTENT)