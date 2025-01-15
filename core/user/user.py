from core.common.events import EventPublisher, ModelCreatedEvent, ModelModifiedEvent
from core.campaign.campaign import Campaign
from .events import DonateEvent, BuyEvent
from typing import Optional
from decimal import Decimal

class User:
    def __init__(self) -> None:
        #TODO
        pass
    
    def change_data(self, email: Optional[str], name: Optional[str], password: Optional[str],
                    phone_number: Optional[str]) -> None:
        #TODO
        EventPublisher.add_event(ModelModifiedEvent[User](self))
        return
    
    def donate(self, campaign: Campaign, amount: Decimal) -> None:
        #TODO
        user_id = ""
        campaign_id = ""
        EventPublisher.add_event(DonateEvent(user_id, campaign_id, amount))
        return
    
    def buy(self, campaign: Campaign) -> None:
        #TODO
        user_id = ""
        product_id = ""
        EventPublisher.add_event(BuyEvent(user_id, product_id))
        return
    
    @classmethod
    def create(cls) -> 'User':
        #TODO
        user : User
        EventPublisher.add_event(ModelCreatedEvent[User](user))
        return user
    
    @classmethod
    def load(cls) -> 'User':
        #TODO
        user : User
        return user