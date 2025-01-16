from core.common.events import EventPublisher, ModelCreatedEvent, ModelModifiedEvent
from core.campaign.campaign import Campaign
from core.common.values import ID
from .events import DonateEvent, BuyEvent
from typing import List, Optional
from decimal import Decimal

class User:
    def __init__(self, user_id: str, email: str, name: str, password: str, phone_number: str, campaigns: List[Campaign]) -> None:
        self.user_id = user_id
        self.email = email
        self.name = name
        self.password = password
        self.phone_number = phone_number
        self.campaigns = campaigns
    
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
    def create(cls, email: str, name: str, password: str, phone_number: str) -> 'User':
        user: User = cls(ID.generate(), email, name, password, phone_number, [])
        EventPublisher.add_event(ModelCreatedEvent[User](user))
        return user
    
    @classmethod
    def load(cls, user_id: str, email: str, name: str, password: str, phone_number: str, campaigns: List[Campaign]) -> 'User':
        #TODO
        user: User = cls(user_id, email, name, password, phone_number, campaigns)
        user : User
        return user
