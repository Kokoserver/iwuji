from tortoise import models, fields as f
from app.utils.password_hasher import Hasher



class User(models.Model):
    id  = f.UUIDField(auto_generate=True, pk=True)
    firstname = f.CharField(max_length=50, required=True)
    lastname = f.CharField(max_length=50, required=True)
    email = f.CharField(max_length=50, required=True, unique=True)
    password = f.CharField(max_length=100, required=True)
    is_active = f.BooleanField(default=False)
    role = f.ForeignKeyField('models.Permission', related_name='users', null=True)
    created_at = f.DatetimeField(auto_now=True)
    

    def hash_password(self)->str:
        self.password = Hasher.hash_password(self.password)
     
    def generate_hash(self, password:str)->str:
        return  Hasher.hash_password(password)
        
    def check_password(self, plain_password:str)->bool:
        check_pass = Hasher.check_password(plain_password, self.password)
        if check_pass:
            return True
        return False
        
        
class Publisher(models.Model):
    id  = f.UUIDField(auto_generate=True, pk=True)
    title = f.CharField(max_length=10, required=True)
    description = f.TextField()
    details = f.ForeignKeyField('models.User', related_name='publisher_details', null=True)
    profile_img = f.ForeignKeyField('models.Media', related_name='publisher_image', null=True)
    
