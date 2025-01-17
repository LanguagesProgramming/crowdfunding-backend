from core.campaign.product import Product
from core.common.events import EventPublisher, ModelCreatedEvent
from .events import AddCampaignImageEvent, DeleteCampaignImageEvent
from core.common.image_storage import Base64SaveStorageImage, DeleteStorageImage
from core.common.values import ID, StringValue
from core.user import user
from .category import CampaignCategory
from typing import List, Optional
from decimal import Decimal

class Campaign:
    FOLDER_NAME = "campaignImages"
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
        self.save_image = Base64SaveStorageImage(self.FOLDER_NAME)
        self.delete_image = DeleteStorageImage(self.FOLDER_NAME)


    def change_data(self, title: Optional[str], category: Optional[CampaignCategory],
                    description: Optional[str]) -> None:
        if title is not None:
            self.title = title
        
        if category is not None:
            self.category = category
        
        if description is not None:
            self.description = description
        
        EventPublisher.add_event(ModelCreatedEvent[Campaign](self))
        return

    def add_current_money(self, amount: Decimal) -> None:
        self.current_money += amount
        EventPublisher.add_event(ModelCreatedEvent[Campaign](self))
        return
    
    def add_image(self, image: str) -> None:
        url = self.save_image.save(image)
        self.images.append(url)
        EventPublisher.add_event(AddCampaignImageEvent(self.id, url))
        return
    
    def delete_image(self, image: str) -> None:
        self.images.remove(image)
        self.delete_image.delete(image)
        EventPublisher.add_event(DeleteCampaignImageEvent(self.id, image))
        return

    def is_same_category(self, category: CampaignCategory) -> bool:
        return self.category == category

    def matches_title(self, title: str):
        return title.lower() in self.title.lower() 
    
    @classmethod
    def create(cls, userId: str, title: str, category: CampaignCategory, description: str, product: Product, goal: Decimal, images: List[str]) -> 'Campaign':
        id = ID.generate()
        product.campaignId = id
        campaign = cls(id, userId, title, category, description, product, goal, Decimal(0), [])
        EventPublisher.add_event(ModelCreatedEvent[Campaign](campaign))
        EventPublisher.add_event(ModelCreatedEvent[Product](product))
        for image in images:
            campaign.add_image(image)
        for image in product.base64_images.copy():
            product.add_image(image)
        return campaign
    
    @classmethod
    def load(cls, id: str, userId: str, title: str, category: CampaignCategory, description: str, product: Product, goal: Decimal, current_money: Decimal, images: List[str]) -> 'Campaign':
        campaign = cls(id, userId, title, category, description, product, goal, current_money, images)
        return campaign
