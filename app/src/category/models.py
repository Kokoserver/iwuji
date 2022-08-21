from tortoise import models, fields as f



class Category(models.Model):
    """_summary_ = "Category"
        description = "Category model for keeping all the base product categories"
    """
    id = f.UUIDField(auto_generate=True, pk=True)
    name = f.CharField(max_length=20, required = True)
    

    
    def __str__(self):
        return self.name
   


    
    
    
    
   

    


  
    






