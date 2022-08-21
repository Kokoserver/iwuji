from tortoise import models, fields as f

class Cart(models.Model):
   """_summary_ = "Cart"
      description = "Cart model for keeping all the cart details"
   """
   id = f.UUIDField(auto_generate=True, pk=True)
   pdf = f.BooleanField(default=False)
   paper_back_qty = f.IntField(default=0)
   hard_back_qty = f.IntField(default=0)
   product = f.ForeignKeyField("models.Product", related_name="product_cart", null = True, blank=True)
   user = f.ForeignKeyField("models.User", related_name="user_cart")
   created_at = f.DatetimeField(auto_now=True)
   
  




  
