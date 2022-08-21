from tortoise import models, fields as f

class AuthModel(models.Model):  
    """_summary_ = "User Auth"
       description = "Model for keeping all the users authorization details"
    """
    id = f.UUIDField(auto_generate=True, pk=True)
    ip = f.CharField(max_length=50, required=True)
    lock_ip = f.BooleanField(default=False)
    verify_login = f.BooleanField(default=False)
    user = f.ForeignKeyField('models.User', related_name='user_auth')
    last_login = f.DatetimeField(auto_now_add=True)
    
   
    
    
    
    
    