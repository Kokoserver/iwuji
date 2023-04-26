from db.model import Base, sa


product_gallery_association_table = sa.Table(
    "product_gallery_association",
    Base.metadata,
    sa.Column(
        "product_media_id",
        sa.ForeignKey("product_media.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    sa.Column(
        "media_id",
        sa.ForeignKey("media.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
product_category_association_table = sa.Table(
    "product_category_association",
    Base.metadata,
    sa.Column(
        "product_id",
        sa.ForeignKey("product.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    sa.Column(
        "category_id",
        sa.ForeignKey("category.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
