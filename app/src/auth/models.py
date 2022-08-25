import typing as t
from app.database.document import BaseMeta, Model, DateMixin, fields as f
from app.src.user.models import User


class AuthModel(Model, DateMixin):  
    """_summary_ = "User Auth"
       description = "Model for keeping all the users authorization details"
    """
    class Meta(BaseMeta):
       tablename: str = "iw_auth"
    ip:str = f.String(max_length=50, nullable=True)
    lock_ip:bool = f.Boolean(default=False)
    verify_login:bool = f.Boolean(default=False)
    user:t.Optional[User] = f.ForeignKey(
       User, 
       related_name="user_auth", 
       ondelete="CASCADE", 
       onupdate="CASCADE")
    
   
    
    
    
    
    