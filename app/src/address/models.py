import typing as t
from app.database.document import BaseMeta, Model, fields as f
from app.src.user.models import User


class ShippingAddress(Model):
    """_summary_ = "Shipping Address"
       description = "Shipping Address model for keeping all the shipping address details"
    """
    class Meta(BaseMeta):
       tablename: str = "iw_shipping_addr"

    user:User = f.ForeignKey(
       User, 
       related_name="user_shipping_address", 
       ondelete="CASCADE", 
       onupdate="CASCADE"
       )
    street:str = f.String(max_length=50)
    city:str = f.String(max_length=20)
    state:str = f.String(max_length=20)
    country:str = f.String(max_length=20)
    tel:str = f.String(max_length=16)
    zipcode:str = f.String(max_length=10)
    
