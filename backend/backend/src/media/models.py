from backend.database.document import BaseMeta, Model, fields as f


class Media(Model):
    """_summary_ = "Media"
         description = "Media model for keeping all the media details"
      """

    class Meta(BaseMeta):
        tablename: str = "iw_media"

    alt: str = f.String(max_length=100, nullable=True)
    url: str = f.String(max_length=150, nullable=True, unique=True)
    content_type: str = f.String(max_length=25, nullable=False)
