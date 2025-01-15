from core.common.events import EventPublisher, ModelCreatedEvent, ModelModifiedEvent
from core.common.image_storage import Base64SaveStorageImage, DeleteStorageImage
from core.common.values import ID, StringValue
from decimal import Decimal
from typing import Optional

class Product:
    def __init__(self) -> None:
        #TODO
        return
        
    def change_data(self, name: Optional[str], price: Optional[Decimal], discoint: Optional[Decimal]) -> None:
        #TODO
        EventPublisher.add_event(ModelModifiedEvent[Product](self))
        return

    def add_image(self, image: str) -> None:
        #TODO
        return
    
    def delete_image(self, image: str) -> None:
        #TODO
        return
    
    @classmethod
    def create(cls) -> 'Product':
        #TODO
        product : Product
        EventPublisher.add_event(ModelCreatedEvent[Product](product))
        return product

    @classmethod
    def load(cls) -> 'Product':
        #TODO
        product : Product
        return product