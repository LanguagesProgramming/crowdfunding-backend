from core.campaign.product import Product
from core.common.events import EventPublisher, ModelCreatedEvent, ModelModifiedEvent
from core.common.image_storage import Base64SaveStorageImage, DeleteStorageImage
from core.common.values import ID, StringValue
from core.user import user
from .category import CampaignCategory
from typing import List, Optional
from decimal import Decimal

class Campaign:
    def __init__(self, id: str, userId: str, title: str, category: CampaignCategory, description: str, product: Product, goal: Decimal, current_money: Decimal, images: List[str]) -> None:
        self.id = id 
        self.userId = userId
        self.title = title
        self.category = category
        self.description = description 
        self.product = product
        self.goal = goal 
        self.current_money = current_money
        self.images = images

    def change_data(self, title: Optional[str], category: Optional[CampaignCategory],
                    description: Optional[str]) -> None:
        #TODO
        EventPublisher.add_event(ModelModifiedEvent[Campaign](self))
        return

    def add_current_money(self, amount: Decimal) -> None:
        #TODO
        return
    
    def add_image(self, image: str) -> None:
        Base64SaveStorageImage.verify_base64(cls, image)
        Base64SaveStorageImage.save(self, image, "Imagenes")
        return
    
    def delete_image(self, image: str) -> None:
        DeleteStorageImage.delete(self, image)
        return

    def is_same_category(self, category: CampaignCategory) -> bool:
        return self.category == category

    def matches_title(self, title: str):
        return title.lower() in self.title.lower() 
    
    @classmethod
    def create(cls, userId: str, title: str, category: CampaignCategory, description: str, product: Product, goal: Decimal, images: List[str]) -> 'Campaign':
        campaign = cls(ID.generate(), userId, title, category, description, product, goal, Decimal(0), images)
        EventPublisher.add_event(ModelCreatedEvent[Campaign](campaign))
        return campaign
    
    @classmethod
    def load(cls, id: str, userId: str, title: str, category: CampaignCategory, description: str, product: Product, goal: Decimal, current_money: Decimal, images: List[str]) -> 'Campaign':
        campaign = cls(id, userId, title, category, description, product, goal, current_money, images)
        return campaign
