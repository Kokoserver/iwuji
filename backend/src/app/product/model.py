import uuid
from db.model import GUID, Base, sa
from sqlalchemy.orm import relationship


from src.app.product.associate_model import (
    product_category_association_table,
    product_gallery_association_table,
)


class ProductProperty(Base):
    __tablename__ = "product_property"
    has_pdf = sa.Column(sa.Boolean, default=True)
    in_stock = sa.Column(sa.Boolean, default=False)
    discount = sa.Column(sa.Float, default=0.0)
    paper_back_price = sa.Column(sa.Numeric(precision=10, scale=2))
    paper_back_qty = sa.Column(sa.Integer, default=0)
    hard_back_price = sa.Column(sa.Numeric(precision=10, scale=2))
    hard_back_qty = sa.Column(sa.Integer, default=0)
    pdf_price = sa.Column(sa.Numeric(precision=10, scale=2))
    product_id = sa.Column(
        GUID,
        sa.ForeignKey("product.id", ondelete="CASCADE"),
        nullable=True,
    )
    product = relationship("Product", back_populates="property", uselist=True)


class ProductAttribute(Base):
    __tablename__ = "product_attribute"
    isbn10 = sa.Column(sa.String(18), nullable=True)
    isbn13 = sa.Column(sa.String(18), nullable=True)
    height = sa.Column(sa.Float, default=0.0)
    width = sa.Column(sa.Float, default=0.0)
    weight = sa.Column(sa.Float, default=0.0)
    pub_date = sa.Column(sa.Date)
    product_id = sa.Column(GUID, sa.ForeignKey("product.id", ondelete="CASCADE"), nullable=True)
    product = relationship(
        "Product",
        back_populates="attribute",
        foreign_keys=[product_id],
        uselist=False,
    )


class ProductMedia(Base):
    __tablename__ = "product_media"
    product_id = sa.Column(
        GUID, sa.ForeignKey("product.id", ondelete="CASCADE"), nullable=True, index=True
    )

    pdf_id = sa.Column(GUID, sa.ForeignKey("media.id", ondelete="SET NULL"))
    cover_img_id = sa.Column(GUID, sa.ForeignKey("media.id", ondelete="SET NULL"))
    gallery = relationship("Media", secondary=product_gallery_association_table)
    product = relationship(
        "Product",
        back_populates="media",
    )
    pdf = relationship("Media", foreign_keys=[pdf_id])
    cover_img = relationship("Media", foreign_keys=[cover_img_id], uselist=False)
    product = relationship("Product", back_populates="medias", uselist=False)


class Product(Base):
    __tablename__ = "product"
    id = sa.Column(
        GUID(),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    name = sa.Column(sa.String(50))
    description = sa.Column(sa.Text)
    slug = sa.Column(sa.String)
    amazon_link = sa.Column(sa.String, nullable=True)
    epub_link = sa.Column(sa.String, nullable=True)
    kindle_link = sa.Column(sa.String, nullable=True)
    is_series = sa.Column(sa.Boolean, default=False)
    is_active = sa.Column(sa.Boolean, default=False)
    is_assigned = sa.Column(sa.Boolean, default=False)
    categories = relationship(
        "Category",
        secondary=product_category_association_table,
    )
    parent_id = sa.Column(
        GUID,
        sa.ForeignKey(
            "product.id",
        ),
        nullable=True,
    )
    variations = relationship(
        "Product",
        backref="parent",
        remote_side=[id],
        lazy="selectin",
    )
    medias = relationship(
        "ProductMedia",
        back_populates="product",
        uselist=False,
        passive_deletes=True,
    )
    attribute = relationship(
        "ProductAttribute",
        back_populates="product",
        uselist=False,
        passive_deletes=True,
    )
    property = relationship(
        "ProductProperty",
        back_populates="product",
        uselist=False,
        passive_deletes=True,
    )
