from tortoise import models, fields as f
from app.src.order.enum import OrderStatus
from app.utils.random_string import generate_orderId


class Order(models.Model): 
      """_summary_ = "Order"
         description = "Order model for keeping all the orders of the user"
      """
      id = f.UUIDField(auto_generate=True, pk=True)
      orderId = f.CharField(max_length=12, default=generate_orderId, index=True,unique=True)
      user = f.ForeignKeyField(model_name="models.User", related_name="user_order")
      shipping_address = f.ForeignKeyField(model_name="models.ShippingAddress", related_name="order_address")
      status =  f.CharEnumField(OrderStatus, required=True, default=OrderStatus.PENDING)
      created_at = f.DatetimeField(auto_now=True)
      
      
class OrderItem(models.Model):
      id = f.UUIDField(auto_generate=True, pk=True)
      pdf_qty = f.IntField(default=0)
      paper_back_qty = f.IntField(default=0)
      hard_back_qty = f.IntField(default=0)
      product = f.ForeignKeyField(model_name="models.Product",)
      order= f.ForeignKeyField(model_name="models.Order")
   
      



  
   
