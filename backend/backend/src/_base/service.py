import ormar


class BaseService:
    @staticmethod
    async def get(model, *args, **kwargs) -> object:
        try:
            obj = await model.objects.get(*args, **kwargs)
            return obj
        except ormar.NoMatch:
            return None

    @staticmethod
    async def get_or_none(model, *args, **kwargs) -> object:
        obj = await model.objects.get_or_none(*args, **kwargs)
        if obj:
            return obj
        return None

    @staticmethod
    async def create(model, *args, **kwargs) -> object:
        obj = await model.objects.create(*args, **kwargs)
        if obj:
            return obj
        return None

    @staticmethod
    async def get_or_create(model, *args, **kwargs) -> object:
        obj = await model.objects.get_or_create(*args, **kwargs)
        if obj:
            return obj
        return None


    @staticmethod
    async def get_or_update(model, *args, **kwargs) -> object:
        obj = await model.objects.get_or_update(*args, **kwargs)
        if obj:
            return obj
        return None


    @staticmethod
    async def update(model, *args, **kwargs) -> object:
        obj = await model.objects.update(*args, **kwargs)
        if obj:
            return obj
        return None

    @staticmethod
    async def update_or_create(model, *args, **kwargs) -> object:
        obj = await model.objects.update(*args, **kwargs)
        if obj:
            return obj
        return None

    @staticmethod
    async def remove(model, *args, **kwargs) -> object:
        obj = await model.objects.remove(*args, **kwargs)
        if obj:
            return obj
        return None


