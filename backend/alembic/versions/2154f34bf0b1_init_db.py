"""init db

Revision ID: 2154f34bf0b1
Revises: 
Create Date: 2023-03-08 21:06:30.315535

"""
from alembic import op
import sqlalchemy as sa
import db

# revision identifiers, used by Alembic.
revision = "2154f34bf0b1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("name", sa.String(length=24), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "media",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("alt", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("content_type", sa.String(length=30), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url"),
    )
    op.create_index(op.f("ix_media_alt"), "media", ["alt"], unique=True)
    op.create_table(
        "permission",
        sa.Column("name", sa.String(length=24), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product",
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("slug", sa.String(), nullable=True),
        sa.Column("amazon_link", sa.String(), nullable=True),
        sa.Column("epub_link", sa.String(), nullable=True),
        sa.Column("kindle_link", sa.String(), nullable=True),
        sa.Column("is_series", sa.Boolean(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_assigned", sa.Boolean(), nullable=True),
        sa.Column("parent_id", db.model.GUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "status",
        sa.Column("name", sa.String(length=24), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("firstname", sa.String(length=20), nullable=True),
        sa.Column("lastname", sa.String(length=20), nullable=True),
        sa.Column("email", sa.String(length=50), nullable=True),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column("tel", sa.String(length=17), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "user_title",
        sa.Column("name", sa.String(length=24), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "address",
        sa.Column("user_id", db.model.GUID(), nullable=True),
        sa.Column("street", sa.String(length=100), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("state", sa.String(length=100), nullable=True),
        sa.Column("postal_code", sa.String(length=10), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "auth_token",
        sa.Column("refresh_token", sa.String(), nullable=True),
        sa.Column("access_token", sa.String(), nullable=True),
        sa.Column("user_id", db.model.GUID(), nullable=True),
        sa.Column("ip_address", sa.String(length=24), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "author",
        sa.Column("firstname", sa.String(length=20), nullable=True),
        sa.Column("lastname", sa.String(length=20), nullable=True),
        sa.Column("email", sa.String(length=50), nullable=True),
        sa.Column("short_description", sa.TEXT(), nullable=True),
        sa.Column("full_description", sa.TEXT(), nullable=True),
        sa.Column("title_id", db.model.GUID(), nullable=True),
        sa.Column("cover_image_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["cover_image_id"], ["media.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["title_id"], ["user_title.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "cart",
        sa.Column("pdf", sa.Boolean(), nullable=True),
        sa.Column("paper_back_qty", sa.Integer(), nullable=True),
        sa.Column("hard_back_qty", sa.Integer(), nullable=True),
        sa.Column("item_id", db.model.GUID(), nullable=False),
        sa.Column("user_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["item_id"], ["product.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product_attribute",
        sa.Column("isbn10", sa.String(length=18), nullable=True),
        sa.Column("isbn13", sa.String(length=18), nullable=True),
        sa.Column("height", sa.Float(), nullable=True),
        sa.Column("width", sa.Float(), nullable=True),
        sa.Column("weight", sa.Float(), nullable=True),
        sa.Column("pub_date", sa.Date(), nullable=True),
        sa.Column("product_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["product_id"], ["product.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "product_category_association",
        sa.Column("product_id", db.model.GUID(), nullable=False),
        sa.Column("category_id", db.model.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["product_id"], ["product.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("product_id", "category_id"),
    )
    op.create_table(
        "product_media",
        sa.Column("product_id", db.model.GUID(), nullable=True),
        sa.Column("pdf_id", db.model.GUID(), nullable=True),
        sa.Column("cover_img_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["cover_img_id"], ["media.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["pdf_id"], ["media.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["product_id"], ["product.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_product_media_product_id"),
        "product_media",
        ["product_id"],
        unique=False,
    )
    op.create_table(
        "product_property",
        sa.Column("has_pdf", sa.Boolean(), nullable=True),
        sa.Column("in_stock", sa.Boolean(), nullable=True),
        sa.Column("discount", sa.Float(), nullable=True),
        sa.Column("paper_back_price", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("paper_back_qty", sa.Integer(), nullable=True),
        sa.Column("hard_back_price", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("hard_back_qty", sa.Integer(), nullable=True),
        sa.Column("pdf_price", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("product_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["product_id"], ["product.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "review",
        sa.Column("comment", sa.String(length=255), nullable=True),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.Column("reviewed", sa.Boolean(), nullable=True),
        sa.Column("edit_limit", sa.Integer(), nullable=True),
        sa.Column("user_id", db.model.GUID(), nullable=True),
        sa.Column("product_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_permissions_association",
        sa.Column("user_id", db.model.GUID(), nullable=False),
        sa.Column("permission_id", db.model.GUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["permission_id"],
            ["permission.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("user_id", "permission_id"),
    )
    op.create_table(
        "order",
        sa.Column("order_id", sa.String(length=15), nullable=True),
        sa.Column("user_id", db.model.GUID(), nullable=True),
        sa.Column("shipping_address_id", db.model.GUID(), nullable=True),
        sa.Column("status_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["shipping_address_id"], ["address.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(["status_id"], ["status.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_order_order_id"), "order", ["order_id"], unique=True)
    op.create_table(
        "product_gallery_association",
        sa.Column("product_media_id", db.model.GUID(), nullable=False),
        sa.Column("media_id", db.model.GUID(), nullable=False),
        sa.ForeignKeyConstraint(["media_id"], ["media.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["product_media_id"], ["product_media.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("product_media_id", "media_id"),
    )
    op.create_table(
        "order_item",
        sa.Column("pdf", sa.Boolean(), nullable=True),
        sa.Column("paper_back_qty", sa.Integer(), nullable=True),
        sa.Column("hard_back_qty", sa.Integer(), nullable=True),
        sa.Column("delivered", sa.Boolean(), nullable=True),
        sa.Column("tracking_id", sa.String(length=10), nullable=True),
        sa.Column("product_id", db.model.GUID(), nullable=True),
        sa.Column("order_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["order_id"], ["order.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_order_item_delivered"), "order_item", ["delivered"], unique=False
    )
    op.create_index(
        op.f("ix_order_item_tracking_id"), "order_item", ["tracking_id"], unique=False
    )
    op.create_table(
        "payments",
        sa.Column("reference", sa.String(length=15), nullable=True),
        sa.Column("total_payed", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("completed", sa.Boolean(), nullable=True),
        sa.Column("order_id", db.model.GUID(), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["order_id"], ["order.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "order_tracking",
        sa.Column("order_item_id", db.model.GUID(), nullable=True),
        sa.Column("location", sa.String(length=50), nullable=True),
        sa.Column("id", db.model.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["order_item_id"], ["order_item.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("order_tracking")
    op.drop_table("payments")
    op.drop_index(op.f("ix_order_item_tracking_id"), table_name="order_item")
    op.drop_index(op.f("ix_order_item_delivered"), table_name="order_item")
    op.drop_table("order_item")
    op.drop_table("product_gallery_association")
    op.drop_index(op.f("ix_order_order_id"), table_name="order")
    op.drop_table("order")
    op.drop_table("user_permissions_association")
    op.drop_table("review")
    op.drop_table("product_property")
    op.drop_index(op.f("ix_product_media_product_id"), table_name="product_media")
    op.drop_table("product_media")
    op.drop_table("product_category_association")
    op.drop_table("product_attribute")
    op.drop_table("cart")
    op.drop_table("author")
    op.drop_table("auth_token")
    op.drop_table("address")
    op.drop_table("user_title")
    op.drop_table("user")
    op.drop_table("status")
    op.drop_table("product")
    op.drop_table("permission")
    op.drop_index(op.f("ix_media_alt"), table_name="media")
    op.drop_table("media")
    op.drop_table("category")
    # ### end Alembic commands ###
