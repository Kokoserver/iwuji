from datetime import datetime
from typing import List, Optional
import pydantic as pd
from app.src.media.schemas import MediaBase
from app.utils import pydanticForm
from app.src.category.schemas import CategoryIn
from app.src.publisher.schemas import PublisherOut

class ProductToVariationBase(pd.BaseModel):
    name : str
    description : str
    slug : str
    


class ProductAttributeIn(pd.BaseModel):
    isbn10: Optional[str] = None
    isbn13: Optional[str] = None
    language: Optional[str] = "english"
    pub_date: Optional[datetime]
    pages: Optional[int]
    height: Optional[float] = 0.0
    width: Optional[float] = 0.0
    weight: Optional[float]    = 0.0

class ProductAttributeOut(ProductAttributeIn):
      pass
      
      
class ProductPropertyIn(pd.BaseModel):
    in_stock : bool = True
    discount :  Optional[float] = 0.0
    paper_back_price : float
    paper_back_qty : int = 1
    hard_back_price  : Optional[float] = 0.0
    hard_back_qty : int = 1
    pdf_price : Optional[float] = 0.0
    
class ProductPropertyOut(ProductPropertyIn):
    pass


                                 

@pydanticForm.as_form
class ProductIn(ProductAttributeIn, ProductPropertyIn):
    name:str = pd.Field(...,description="Product name", max_length=300)
    description :str = pd.Field(...,description="Product description", max_length=1000)
    categories:str = pd.Field(...,description="Product categories", max_length=1000)
    is_series:Optional[bool] = False
    is_active :Optional[bool] = True
    is_assigned :Optional[bool ]= False
    
   

@pydanticForm.as_form
class VariationIn(pd.BaseModel):
    name: str = pd.Field(..., description="Variation name", max_length=300)
    description : str = pd.Field(..., description="Variation description", max_length=1000)
    is_active:Optional[bool] = True

class VariationProductIn(pd.BaseModel):
    productId:int 
    variationId:int

class VariationProductUpdateIn(VariationProductIn):
    remove_books:bool = False
    


class ProductOut(ProductToVariationBase):
    id:int
    is_series : bool  
    publisher: Optional[PublisherOut]
    # pdf_file: Optional[MediaBase]
    cover_img: Optional[MediaBase]
    categories : List[CategoryIn]
    property  : ProductPropertyOut
    attribute : ProductAttributeOut
    cover_img : Optional[MediaBase]
    gallery  : Optional[List[MediaBase]]
    created_at  : datetime

 
class VariationOut(ProductToVariationBase):
    id:int
    cover_img: Optional[MediaBase]
    items : List[ProductOut]
    created_at :datetime
    
