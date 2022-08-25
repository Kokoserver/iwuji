from app.src.media.models import Media
import typing as t
from app.database.document import  BaseMeta, Model, fields as f
from app.src.publisher.enum import PublisherTitle
from app.src.user.models import User

        
class Publisher(Model):
    class Meta(BaseMeta):
       tablename: str = "iw_publisher"
    title:str = f.String(choices=PublisherTitle, max_length=10, nullable=True, default=PublisherTitle.DR)
    description:str = f.Text()
    info:t.Optional[User] = f.ForeignKey(User, related_name='publisher_details', nullable=True)
    profile_img = f.ForeignKey(
       Media, 
       related_name='publisher_image', 
      ondelete="SET NULL", 
       onupdate="CASCADE")
    
