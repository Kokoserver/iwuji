from tortoise import models, fields as f
from app.src.payment.enum import PaymentStatus, PaymentMethod, PaymentCurrency

class Payment(models.Model):
    """_summary_ = "Payment"
    description = "Payment model for keeping all the payments of the user"
    """
    id = f.UUIDField(auto_generate=True, pk=True)
    pay_ref = f.CharField(max_length=12, index=True,unique=True)
    amount =  f.DecimalField(max_digits=10, decimal_places=2, required=True)
    currency = f.CharField(max_length=20, required=True, choices=PaymentCurrency, default=PaymentCurrency.USD)
    method =  f.CharField(max_length=20, required=True, choices=PaymentMethod, default=PaymentMethod.CARD)
    status =  f.CharField(max_length=20, required=True, choices=PaymentStatus, default=PaymentStatus.PENDING)
    order =  f.ForeignKeyField("models.Order", related_name="order_payment")
    user = f.ForeignKeyField("models.User", related_name="user_payment")
    created_at = f.DatetimeField(auto_now=True)
    update_at = f.DatetimeField(auto_now_add=True)


    

  
    

   

   

    
  

    