from datetime import datetime
import typing as t
from app.database.document import BaseMeta, DateMixin, Model, fields as f
from pydantic import condecimal as dc
from slugify import slugify
from app.src.category.models import Category

from app.src.media.models import Media
from app.src.publisher.models import Publisher


class ProductProperty(Model):
    """_summary_ = "Product Attribute"
        description = "Product Attribute model for keeping all the product attributes"
    """
    class Meta(BaseMeta):
         tablename: str = "iw_product_property"
    in_stock:bool = f.Boolean(default=True)
    discount:float = f.Float(default=0.0)
    paper_back_price:dc(max_digits=10, decimal_places=2)  = f.Decimal(max_digits=10, decimal_places=2, default=0.0)
    paper_back_qty:float = f.Integer(default=0)
    hard_back_price:dc(max_digits=10, decimal_places=2)  = f.Decimal(max_digits=10, decimal_places=2, default=0.0)
    hard_back_qty :int = f.Integer(default=0)
    pdf_price:dc(max_digits=10, decimal_places=2)  = f.Decimal(max_digits=10, decimal_places=2, default=0.0)

    
    
    
class ProductAttribute(Model):
    class Meta(BaseMeta):
         tablename: str = "iw_product_attr"
    isbn10:str = f.String(max_length=10, nullable=True) 
    isbn13:str = f.String(max_length=13, nullable=True)
    language:str = f.String(max_length=10, nullable=True, default="english")
    pub_date:datetime = f.DateTime(nullable=True)
    pages:int = f.Integer(default=0)
    height:float = f.Float(required=False)
    width:float = f.Float(required=False)
    weight:float = f.Float(required=False)

        
    
        




################################### start of product############################################
class Product(Model, DateMixin):
    """_summary_ = "Product"
        description = "Product model for keeping all the products"
    """
    class Meta(BaseMeta):
        tablename: str= "iw_product"
       
    name:str = f.String(max_length=50, nullable=True)
    description:str = f.Text(nullable=True)
    slug:str = f.String(max_length=50, nullable=True) 
    is_series:bool = f.Boolean(default=False)   
    is_assigned:bool = f.Boolean(default=False)
    is_active:bool = f.Boolean(default=True)
    pdf_file:t.Optional[Media] = f.ForeignKey(
        Media, 
        related_name="product_pdf_file", 
       ondelete="SET NULL", 
        onupdate="CASCADE",
        nullable=True
        )
    publisher:t.Optional[Publisher] = f.ForeignKey(
        Publisher, 
        related_name="publisher", 
        nullable=True, 
       ondelete="SET NULL", 
        onupdate="CASCADE",
        )
    categories:t.Optional[t.List[Category]] = f.ManyToMany(
        Category, 
        related_name="product_category", 
        ondelete="CASCADE", 
        onupdate="CASCADE")
    property:t.Optional[ProductProperty] = f.ForeignKey(
        ProductProperty, 
        related_name="product_property", 
       ondelete="SET NULL", 
        onupdate="CASCADE",
        nullable=True
        )
    attribute:t.Optional[ProductAttribute] = f.ForeignKey(
        ProductAttribute, 
        related_name="product_to_attribute",
       ondelete="SET NULL", 
        onupdate="CASCADE",
        nullable=True
        )
    cover_img:t.Optional[t.Union[Media, t.Dict]] = f.ForeignKey(
        Media, 
        related_name="product_cover_img", 
       ondelete="SET NULL", 
        onupdate="CASCADE",
        nullable=True
        )
    gallery:t.Optional[t.List[Media]] = f.ManyToMany(
        Media, 
        related_name="product_gallery", 
        ondelete="CASCADE", 
        onupdate="CASCADE", 
        nullable=True
        )
    
        
    def make_slug(self):
        self.slug = slugify(self.name, max_length=50)
     
################################### end of product############################################

class Variation(Model, DateMixin):
    class Meta(BaseMeta):
        tablename:str = "iw_product_variation"
    name:str = f.String(max_length=100, nullable=True)
    description:str = f.String(max_length=100, nullable=True)
    slug:str = f.String(max_length=50, nullable=True)
    is_active:bool = f.Boolean(default=True)
    cover_img:t.Optional[Media] = f.ForeignKey(
        Media, 
        related_name="series_cover_img", 
        ondelete="SET NULL",
        onupdate="CASCADE",
        nullable=True
        )
    items:t.Optional[t.List[Product]] = f.ManyToMany(
        Product, 
        related_name="variation_items",
        ondelete="CASCADE", 
        onupdate="CASCADE", 
        )
    
    def make_slug(self):
        self.slug = slugify(self.name, max_length=50)
        
    
        
    
