from core.campaign import campaign
from core.common.events import EventPublisher, ModelCreatedEvent, ModelModifiedEvent
from core.common.image_storage import Base64SaveStorageImage, DeleteStorageImage
from core.common.values import ID, StringValue
from decimal import Decimal
from typing import List, Optional

class Product:
    def __init__(self, id: str, name: str, price: Decimal, discount: Decimal, campaignId: str, images: List[str]) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        self.campaignId = campaignId
        self.images = images
        
    def change_data(self, name: Optional[str], price: Optional[Decimal], discount: Optional[Decimal]) -> None:
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
    def create(cls, name: str, price: Decimal, discount: Decimal, images: List[str]) -> 'Product':
        product: Product = cls(ID.generate(), name, price, discount, None, images) 
        return product

    @classmethod
    def load(cls, id: str, name: str, price: Decimal, discount: Decimal, campaignId: str, images: List[str]) -> 'Product':
        product: Product = cls(id, name, price, discount, campaignId, images)
        return product
