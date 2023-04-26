from src.app.tracking.model import Tracking
from src.base.repository.base_repository import BaseRepository
from src.app.order import model


class OrderItemRepository(BaseRepository[model.OrderItem]):
    def __init__(self):
        super().__init__(model.OrderItem)

    async def add_track(self, order_item: model.OrderItem, track: Tracking):
        order_item.trackings.extends(track)
        self.db.add(order_item)
        await self.db.commit()
        self.db.refresh(order_item)
        return order_item


class OrderRepository(BaseRepository[model.Order]):
    def __init__(self):
        super().__init__(model.Order)


order_repo = OrderRepository()
order_item_repo = OrderItemRepository()
