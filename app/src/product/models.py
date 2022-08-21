from tortoise import models, Tortoise, fields as f
from slugify import slugify
from app.src.category.models import Category

from app.src.media.models import Media


class ProductProperty(models.Model):
    """_summary_ = "Product Attribute"
        description = "Product Attribute model for keeping all the product attributes"
    """
    id = f.UUIDField(auto_generate=True, pk=True)
    in_stock = f.BooleanField(default=True)
    discount = f.FloatField(default=0.0)
    paper_back_price = f.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    paper_back_qty = f.IntField(default=0)
    hard_back_price = f.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    hard_back_qty = f.IntField(default=0)
    pdf_price = f.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    product:f.ReverseRelation["Product"]
    
    class PydanticMeta:
        exclude = ('product',)
    
    
    
class ProductAttribute(models.Model):
    id = f.UUIDField(auto_generate=True, pk=True)
    isbn10 = f.CharField(max_length=10, null=True) 
    isbn13 = f.CharField(max_length=13, null=True)
    language = f.CharField(max_length=10, null=True, default="english")
    pub_date = f.DateField(null=True)
    pages = f.IntField(default=0)
    height = f.FloatField(required=False)
    width = f.FloatField(required=False)
    weight = f.FloatField(required=False)
    created_at = f.DatetimeField(auto_now=True)
    updated_at = f.DatetimeField(auto_now_add=True)
    product:f.ReverseRelation["Product"]
    
    class PydanticMeta:
        exclude = ('product',)
    

    


class Variation(models.Model):
    id = f.UUIDField(auto_generate=True, pk=True)
    name = f.CharField(max_length=100, null=True)
    description = f.CharField(max_length=100, null=True)
    slug = f.CharField(max_length=50, null=True)
    is_active = f.BooleanField(default=True)
    cover_img:f.ForeignKeyRelation["Media"] = f.ForeignKeyField("models.Media", related_name="series_cover_img")
    items:f.ManyToManyRelation["Product"] = f.ManyToManyField("models.Product", through="variation_items", related_name="variation_to_product")
    created_at = f.DatetimeField(auto_now=True)
    updated_at = f.DatetimeField(auto_now_add=True)
    
 
    
    def make_slug(self):
        self.slug = slugify(self.name, max_length=50)
        
    
        




################################### start of product############################################
class Product(models.Model):
    """_summary_ = "Product"
        description = "Product model for keeping all the products"
    """
    id = f.UUIDField(auto_generate=True, pk=True)
    name = f.CharField(max_length=50, required=True)
    description = f.TextField(required=True)
    slug = f.CharField(max_length=50, required=True) 
    is_series = f.BooleanField(default=False)   
    is_active = f.BooleanField(default=True)
    is_assigned = f.BooleanField(default=False)
    pdf_file:f.ForeignKeyRelation["Media"] = f.ForeignKeyField("models.Media", related_name="product_pdf_file")
    # publisher = f.ForeignKeyField("models.Publisher", related_name="publisher", null=True)
    categories:f.ManyToManyRelation["Category"] = f.ManyToManyField("models.Category", related_name="product_category", through="product_to_category")
    property:f.ForeignKeyRelation[ProductProperty] = f.ForeignKeyField("models.ProductProperty", related_name="product_property")
    attribute:f.ForeignKeyRelation[ProductAttribute] = f.ForeignKeyField("models.ProductAttribute", related_name="product_to_attribute")
    cover_img = f.ForeignKeyField("models.Media", related_name="product_cover_img")
    gallery:f.ManyToManyRelation["Media"] = f.ManyToManyField("models.Media", related_name="product_gallery", through="product_to_gallery")
    variation:f.ReverseRelation["Variation"]
    
    class PydanticMeta:
        exclude = ('variation',)
    
    
    created_at = f.DatetimeField(auto_now=True)
    updated_at = f.DatetimeField(auto_now_add=True)

    
    def make_slug(self):
        self.slug = slugify(self.name, max_length=50)
     
################################### end of product############################################


Tortoise.init_models(["app.src.product.models"], "models")