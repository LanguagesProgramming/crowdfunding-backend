from core.campaign import campaign
from core.common.events import EventPublisher, ModelCreatedEvent
from .events import AddProductImageEvent, DeleteProductImageEvent
from core.common.image_storage import Base64SaveStorageImage, DeleteStorageImage
from core.common.values import ID, StringValue
from decimal import Decimal
from typing import List, Optional

class Product:
    FOLDER_NAME = "productImages"
    def __init__(self, id: str, name: str, price: Decimal, discount: Decimal, campaignId: str, images: List[str]) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.discount = discount
        self.campaignId = campaignId
        self.images = images
        self.save_image = Base64SaveStorageImage(self.FOLDER_NAME)
        self.delete_image = DeleteStorageImage(self.FOLDER_NAME)
        self.base64_images = []
        
    def change_data(self, name: Optional[str], price: Optional[Decimal], discount: Optional[Decimal]) -> None:
        if name is not None:
            self.name = name
        
        if price is not None:
            self.price = price
        
        if discount is not None:
            self.discount = discount
        
        EventPublisher.add_event(ModelCreatedEvent[Product](self))
        return

    def add_image(self, image: str) -> None:
        url = self.save_image.save(image)
        self.images.append(url)
        EventPublisher.add_event(AddProductImageEvent(self.id, url))
        return
    
    def delete_image(self, image: str) -> None:
        self.images.remove(image)
        self.delete_image.delete(image)
        EventPublisher.add_event(DeleteProductImageEvent(self.id, image))
        return
    
    @classmethod
    def create(cls, name: str, price: Decimal, discount: Decimal, images: List[str]) -> 'Product':
        product: Product = cls(ID.generate(), name, price, discount, None, [])
        product.base64_images = images
        return product

    @classmethod
    def load(cls, id: str, name: str, price: Decimal, discount: Decimal, campaignId: str, images: List[str]) -> 'Product':
        product: Product = cls(id, name, price, discount, campaignId, images)
        return product
