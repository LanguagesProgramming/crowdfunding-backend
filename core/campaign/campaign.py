from core.common.events import EventPublisher, ModelCreatedEvent, ModelModifiedEvent
from core.common.image_storage import Base64SaveStorageImage, DeleteStorageImage
from core.common.values import ID, StringValue
from .category import CampaignCategory
from typing import Optional
from decimal import Decimal

class Campaign:
    def __init__(self) -> None:
        #TODO
        return
        
    def change_data(self, title: Optional[str], category: Optional[CampaignCategory],
                    description: Optional[str]) -> None:
        #TODO
        EventPublisher.add_event(ModelModifiedEvent[Campaign](self))
        return
    
    def add_current_money(self, amount: Decimal) -> None:
        #TODO
        return
    
    def add_image(self, image: str) -> None:
        #TODO
        return
    
    def delete_image(self, image: str) -> None:
        #TODO
        return
    
    @classmethod
    def create(cls) -> 'Campaign':
        #TODO
        campaign : Campaign
        EventPublisher.add_event(ModelCreatedEvent[Campaign](campaign))
        return campaign
    
    @classmethod
    def load(cls) -> 'Campaign':
        #TODO
        campaign : Campaign
        return campaign