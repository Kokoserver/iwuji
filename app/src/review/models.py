from tortoise import models, fields as f


class Review(models.Model):
    id = f.UUIDField(auto_generate=True, pk=True)
    comment = f.TextField(required=True)
    rating = f.SmallIntField(required=True)
    user = f.ForeignKeyField('models.User', related_name='user_reviews')
    product = f.ForeignKeyField('models.Product', related_name='product_reviews')
    created_at = f.DatetimeField(auto_now=True)
