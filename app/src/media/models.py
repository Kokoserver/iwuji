from tortoise import Tortoise, models, fields as f



class Media(models.Model):
      
      """_summary_ = "Media"
         description = "Media model for keeping all the media details"
      """
      id = f.UUIDField(auto_generate= True, pk=True)
      alt = f.CharField(max_length=100, required=True)
      url = f.CharField(max_length=200, required=True, unique=True)
      content_type = f.CharField(max_length=40, required=True)


      
Tortoise.init_models(["app.src.media.models"], "models")
      
      
      

      