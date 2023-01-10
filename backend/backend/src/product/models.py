from datetime import datetime
import typing as t
from backend.database.document import BaseMeta, DateMixin, Model, fields as f
from ormar.decorators.signals import pre_update
from pydantic import condecimal as dc
from slugify import slugify
from backend.src.category.models import Category
from ormar import pre_save
from backend.utils.discount_calculator import calculate_discount
from backend.src.media.models import Media


class ProductProperty(Model):
    """_summary_ = "Product Attribute"
        description = "Product Attribute model for keeping all the product attributes"
    """

    class Meta(BaseMeta):
        tablename: str = "iw_product_property"

    in_stock: bool = f.Boolean(default=True)
    discount: float = f.Float(default=0.0)
    paper_back_price: dc(max_digits=10, decimal_places=2) = f.Decimal(
        max_digits=10, decimal_places=2, default=0.0)
    paper_back_qty: float = f.Integer(default=0)
    hard_back_price: dc(max_digits=10, decimal_places=2) = f.Decimal(
        max_digits=10, decimal_places=2, default=0.0)
    hard_back_qty: int = f.Integer(default=0)
    pdf_price: dc(max_digits=10, decimal_places=2) = f.Decimal(
        max_digits=10, decimal_places=2, default=0.0)


class ProductAttribute(Model):
    class Meta(BaseMeta):
        tablename: str = "iw_product_attr"

    isbn10: str = f.String(max_length=10, nullable=True)
    isbn13: str = f.String(max_length=13, nullable=True)
    language: str = f.String(max_length=10, nullable=True, default="english")
    pub_date: datetime = f.DateTime(nullable=True)
    pages: int = f.Integer(default=0)
    height: float = f.Float(required=False)
    width: float = f.Float(required=False)
    weight: float = f.Float(required=False)


################################### start of product############################################
class Product(Model, DateMixin):
    """_summary_ = "Product"
        description = "Product model for keeping all the products"
    """

    class Meta(BaseMeta):
        tablename: str = "iw_product"

    name: str = f.String(max_length=50, nullable=True)
    description: str = f.Text(nullable=True)
    slug: str = f.String(max_length=50, nullable=True)
    is_series: bool = f.Boolean(default=False)
    is_assigned: bool = f.Boolean(default=False)
    is_active: bool = f.Boolean(default=True)
    pdf_file: t.Optional[Media] = f.ForeignKey(
        Media,
        related_name="product_pdf_file",
        ondelete="SET NULL",

        nullable=True
    )

    categories: t.Optional[t.List[Category]] = f.ManyToMany(
        Category,
        related_name="product_category",
        ondelete="CASCADE",
        onupdate="CASCADE")
    property: t.Optional[ProductProperty] = f.ForeignKey(
        ProductProperty,
        related_name="product_property",
        ondelete="SET NULL",
        nullable=True
    )
    attribute: t.Optional[ProductAttribute] = f.ForeignKey(
        ProductAttribute,
        related_name="product_to_attribute",
        ondelete="SET NULL",

        nullable=True
    )
    cover_img: t.Optional[t.Union[Media, t.Dict]] = f.ForeignKey(
        Media,
        related_name="product_cover_img",
        ondelete="SET NULL",
        nullable=True
    )
    gallery: t.Optional[t.List[Media]] = f.ManyToMany(
        Media,
        related_name="product_gallery",
        ondelete="CASCADE",
        nullable=True
    )


################################### end of product############################################


class Variation(Model, DateMixin):
    class Meta(BaseMeta):
        tablename: str = "iw_product_variation"

    name: str = f.String(max_length=100, nullable=True)
    description: str = f.String(max_length=100, nullable=True)
    slug: str = f.String(max_length=50, nullable=True)
    is_active: bool = f.Boolean(default=True)
    cover_img: t.Optional[Media] = f.ForeignKey(
        Media,
        related_name="series_cover_img",
        ondelete="SET NULL",

        nullable=True
    )
    items: t.Optional[t.List[Product]] = f.ManyToMany(
        Product,
        related_name="variation_items",
        ondelete="CASCADE",

    )


@pre_save(ProductProperty)
async def calculate_discount_price(sender, instance, **kwargs):
    instance.paper_back_price = calculate_discount(
        instance.paper_back_price, instance.discount)
    instance.hard_back_price = calculate_discount(
        instance.hard_back_price, instance.discount)
    instance.pdf_price = calculate_discount(instance.pdf_price, instance.discount)


@pre_update(ProductProperty)
async def calculate_discount_price(sender, instance, **kwargs):
    instance.paper_back_price = calculate_discount(
        instance.paper_back_price, instance.discount)
    instance.hard_back_price = calculate_discount(
        instance.hard_back_price, instance.discount)
    instance.pdf_price = calculate_discount(instance.pdf_price, instance.discount)


@pre_save(Product)
async def create_product_slug_before_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)


@pre_update(Product)
async def update_product_slug_before_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)


@pre_save(Variation)
async def create_variation_slug_before_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)


@pre_update(Variation)
async def update_variation_slug_before_save(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)
