from backend.database.document import BaseMeta, Model, fields as f


class Category(Model):
    """_summary_ = "Category"
        description = "Category model for keeping all the base product categories"
    """

    class Meta(BaseMeta):
        tablename: str = "iw_category"

    name: str = f.String(max_length=20, nullable=False, unique=True)
