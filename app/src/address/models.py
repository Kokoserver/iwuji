from tortoise import models, fields as f


class ShippingAddress(models.Model):
    id = f.UUIDField(auto_generate=True, pk=True)
    user = f.ForeignKeyField('models.User', related_name='user_address')
    street = f.CharField(max_length=50, required=True)
    city = f.CharField(max_length=50, required=True)
    state = f.CharField(max_length=50, required=True)
    country = f.CharField(max_length=50, required=True)
    tel = f.CharField(max_length=50, required=True)
    zipcode = f.CharField(max_length=50, required=True)
    
