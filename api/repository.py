from core.common.repository import GetModel, SaveModel, ExistsModel, DeleteModel
from core.common.events import EventPublisher, EventSubscriber
from core.user.user import User
from core.user.events import DonateEvent, BuyEvent
from core.campaign.campaign import Campaign
from core.campaign.product import Product
from decimal import Decimal
from typing import List, Type

class DjangoGetUser(GetModel[User]):
    def get(self, user_id: str) -> User:
        #TODO
        user : User
        return user
    
    def get_all(self) -> List[User]:
        #TODO
        users : List[User]
        return users


class DjangoSaveUser(SaveModel[User]):
    def __init__(self) -> None:
        super().__init__(User)
        
    def save(self, user: User) -> None:
        #TODO
        return


class DjangoExistsUser(ExistsModel):
    def exists(self, user_id: str) -> bool:
        #TODO
        return False


class DjangoGetCampaign(GetModel[Campaign]):
    def get(self, campaign_id: str) -> Campaign:
        #TODO
        campaign : Campaign
        return campaign
    
    def get_all(self) -> List[Campaign]:
        #TODO
        campaigns : List[Campaign]
        return campaigns


class DjangoSaveCampaign(SaveModel[Campaign]):
    def __init__(self) -> None:
        super().__init__(Campaign)
        
    def save(self, campaign: Campaign) -> None:
        #TODO
        return


class DjangoDeleteCampaign(DeleteModel[Campaign]):
    def delete(self, campaign_id: str) -> Campaign:
        #TODO
        campaign : Campaign
        return campaign


class DjangoGetProduct(GetModel[Product]):
    def get(self, product_id: str) -> Product:
        #TODO
        product : Product
        return product
    
    def get_all(self) -> List[Product]:
        #TODO
        products : List[Product]
        return products


class DjangoSaveProduct(SaveModel[Product]):
    def __init__(self) -> None:
        super().__init__(Product)
        
    def save(self, product: Product) -> None:
        #TODO
        return


class DjangoSaveDonation(EventSubscriber[DonateEvent]):
    def __init__(self) -> None:
        super().__init__(DonateEvent)
        
    def save(self, user_id: str, campaign_id: str, amount: Decimal) -> None:
        #TODO
        return
    
    def handle(self, event: DonateEvent) -> None:
        #TODO
        user_id = ""
        campaign_id = ""
        amount = Decimal(0)
        self.save(user_id, campaign_id, amount)


class DjangoSavePurchase(EventSubscriber[BuyEvent]):
    def __init__(self) -> None:
        super().__init__(BuyEvent)
        
    def save(self, user_id: str, product_id: str) -> None:
        #TODO
        return
    
    def handle(self, event: BuyEvent) -> None:
        #TODO
        user_id = ""
        product_id = ""
        self.save(user_id, product_id)


EventPublisher.subscribe(DjangoSaveUser())
EventPublisher.subscribe(DjangoSaveCampaign())
EventPublisher.subscribe(DjangoSaveProduct())
EventPublisher.subscribe(DjangoSaveDonation())
EventPublisher.subscribe(DjangoSavePurchase())