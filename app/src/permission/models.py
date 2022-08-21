from tortoise import models,Tortoise, fields as f


class Permission(models.Model):
    id = f.UUIDField(auto_generate=True, pk=True)
    name = f.CharField(max_length=50, required=True)
    created_at = f.DatetimeField(auto_now=True)

Tortoise.init_models(["app.src.permission.models"], "models")
    
