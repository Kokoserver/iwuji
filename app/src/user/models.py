import typing as t
from pydantic import EmailStr
from app.database.document import  BaseMeta, DateMixin, Model, fields as f
from app.src.permission.models import Permission
from app.utils.password_hasher import Hasher



class User(Model, DateMixin):
    class Meta(BaseMeta):
       tablename: str = "iw_user"
    firstname:str = f.String(max_length=50, nullable=True)
    lastname:str = f.String(max_length=50, nullable=True)
    email:EmailStr = f.String(max_length=50, nullable=True, unique=True)
    password:str = f.String(max_length=100, nullable=True)
    is_active:bool = f.Boolean(default=False)
    role:t.Optional[Permission] = f.ForeignKey(
        Permission, 
        related_name='users',
        nullable=True,  
       ondelete="SET NULL", 
       onupdate="CASCADE")


    def hash_password(self)->str:
        self.password = Hasher.hash_password(self.password)
     
    def generate_hash(self, password:str)->str:
        return  Hasher.hash_password(password)
        
    def check_password(self, plain_password:str)->bool:
        check_pass = Hasher.check_password(plain_password, self.password)
        if check_pass:
            return True
        return False
        
        

