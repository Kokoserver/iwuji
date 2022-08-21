from datetime import datetime
from typing import List, Optional
from uuid import UUID
import pydantic as pd
from tortoise.contrib.pydantic import pydantic_model_creator
from app.src.media.schemas import MediaBase
from app.src.product.models import Product, Variation
from app.utils import pydanticForm
from app.src.category.schemas import CategoryIn
# from app.src.publisher.schemas import PublisherOut

class ProductToVariationBase(pd.BaseModel):
    name : str
    description : str
    slug : str
    


class ProductAttributeIn(pd.BaseModel):
    isbn10: Optional[str]
    isbn13: Optional[str]
    language: Optional[str] = "english"
    pub_date: Optional[datetime]
    pages: Optional[int]
    height: Optional[float] = 0.0
    width: Optional[float] = 0.0
    weight: Optional[float]    = 0.0

class ProductAttributeOut(ProductAttributeIn):
      id: UUID
      created_at: Optional[datetime]
      updated_at: Optional[datetime]
      
      
class ProductPropertyIn(pd.BaseModel):
    in_stock : bool = True
    discount :  Optional[float] = 0.0
    paper_back_price : float
    paper_back_qty : int = 1
    hard_back_price  : Optional[float] = 0.0
    hard_back_qty : int = 1
    pdf_price : Optional[float] = 0.0
    
class ProductPropertyOut(ProductPropertyIn):
    id : UUID


                                 

@pydanticForm.as_form
class ProductIn(ProductAttributeIn, ProductPropertyIn):
    name:str = pd.Field(...,description="Product name", max_length=300)
    description :str = pd.Field(...,description="Product description", max_length=1000)
    categories:str = pd.Field(...,description="Product categories", max_length=1000)
    is_series:bool = False
    is_active :bool = True
    is_assigned :bool = False
    
   

@pydanticForm.as_form
class VariationIn(pd.BaseModel):
    name: str = pd.Field(..., description="Variation name", max_length=300)
    description : str = pd.Field(..., description="Variation description", max_length=1000)

class VariationProductIn(pd.BaseModel):
    productId:UUID 
    variationId:UUID

class VariationProductUpdateIn(VariationProductIn):
    remove_books:bool = False
    


class ProductOut(ProductToVariationBase):
    id: UUID
    is_series : bool  
    # publisher: Optional[PublisherOut]
    # pdf_file: Optional[MediaBase]
    cover_img: Optional[MediaBase]
    categories : List[CategoryIn]
    property  : ProductPropertyOut
    attribute : ProductAttributeOut
    cover_img : MediaBase
    gallery  : Optional[List[MediaBase]]
    created_at  : datetime

 
class VariationOut(ProductToVariationBase):
    id: UUID
    cover_img: MediaBase
    items : List[ProductOut]
    created_at :datetime
    
ProductPydanticOut = pydantic_model_creator(Product, name="productOut", exclude=["is_assigned"])
VariationPydanticOut = pydantic_model_creator(Variation, name="variationOut")