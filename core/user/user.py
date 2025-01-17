from core.common.events import EventPublisher, ModelCreatedEvent
from core.campaign.campaign import Campaign
from core.common.values import ID
from .events import DonateEvent, BuyEvent
from typing import List, Optional
from decimal import Decimal
from .values import UserPassword

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
        if email is not None:
            self.email = email
        
        if name is not None:
            self.name = name
        
        if password is not None:
            self.password = password

        if phone_number is not None:
            self.phone_number = phone_number
        
        EventPublisher.add_event(ModelCreatedEvent[User](self))
        return
    
    def donate(self, campaign: Campaign, amount: Decimal) -> None:
        campaign.add_current_money(amount)
        user_id = self.user_id
        campaign_id = campaign.campaign_id
        EventPublisher.add_event(DonateEvent(user_id, campaign_id, amount))
        return
    
    def buy(self, campaign: Campaign) -> None:
        product = campaign.product
        campaign.add_current_money(product.price)
        user_id = self.user_id
        product_id = product.id
        EventPublisher.add_event(BuyEvent(user_id, product_id))
        return
    
    def verify_password(self, password: str) -> bool:
        decoded = UserPassword.decode(self.password)
        return decoded == password

    @classmethod
    def create(cls, email: str, name: str, password: str, phone_number: str) -> 'User':
        user: User = cls(ID.generate(), email, name, password, phone_number, [])
        EventPublisher.add_event(ModelCreatedEvent[User](user))
        return user
    
    @classmethod
    def load(cls, user_id: str, email: str, name: str, password: str, phone_number: str, campaigns: List[Campaign]) -> 'User':
        user: User = cls(user_id, email, name, password, phone_number, campaigns)
        user : User
        return user
