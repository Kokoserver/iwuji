from tortoise import models, fields as f
from app.src.publisher.enum import PublisherTitle

        
class Publisher(models.Model):
    id  = f.UUIDField(auto_generate=True, pk=True)
    title = f.CharEnumField(enum_type=PublisherTitle, max_length=10, required=True, default=PublisherTitle.DR)
    description = f.TextField()
    details = f.ForeignKeyField('models.User', related_name='publisher_details', null=True)
    profile_img = f.ForeignKeyField('models.Media', related_name='publisher_image', null=True)
    
