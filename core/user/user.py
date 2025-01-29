from core.common.events import EventPublisher, ModelCreatedEvent
from core.common.values import ID
from core.campaign.campaign import Campaign
from core.common.values import ID
from .events import DonateEvent, BuyEvent
from typing import List, Optional
from decimal import Decimal
from .values import UserPassword, UserEmail, UserName, UserPhoneNumber

class User:
    def __init__(self, user_id: str, email: str, name: str, password: str, phone_number: str, campaigns: List[Campaign]) -> None:
        self.user_id = ID(user_id).get_value()
        self.email = UserEmail(email).get_value()
        self.name = UserName(name).get_value()
        self.password = UserPassword(password).get_value()
        self.phone_number = UserPhoneNumber(phone_number).get_value()
        self.campaigns = campaigns
    
    def change_data(self, email: Optional[str], name: Optional[str], password: Optional[str],
                    phone_number: Optional[str]) -> None:
        if email is not None:
            self.email = UserEmail(email).get_value()
        
        if name is not None:
            self.name = UserName(name).get_value()
        
        if password is not None:
            self.password = UserPassword(password).get_value()

        if phone_number is not None:
            self.phone_number = UserPhoneNumber(phone_number).get_value()
        
        EventPublisher.add_event(ModelCreatedEvent[User](self))
        return
    
    def donate(self, campaign: Campaign, amount: Decimal) -> None:
        campaign.add_current_money(amount)
        user_id = self.user_id
        campaign_id = campaign.id
        EventPublisher.add_event(DonateEvent(user_id, campaign_id, amount))
        return
    
    def buy(self, campaign: Campaign, stock: int) -> None:
        product = campaign.product
        price = product.price*(1-product.discount)*stock
        campaign.add_current_money(price)
        user_id = self.user_id
        product_id = product.id
        EventPublisher.add_event(BuyEvent(user_id, product_id, stock, price))
        return
    
    def verify_password(self, password: str) -> bool:
        return UserPassword.verify(password, self.password)

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
