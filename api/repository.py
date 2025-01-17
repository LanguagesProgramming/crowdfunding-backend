from core.common.repository import GetModel, SaveModel, ExistsModel, DeleteModel
from core.common.events import EventPublisher, EventSubscriber
from core.user.user import User
from core.user.events import DonateEvent, BuyEvent
from core.campaign.events import AddCampaignImageEvent, AddProductImageEvent, DeleteCampaignImageEvent, DeleteProductImageEvent
from core.campaign.campaign import Campaign
from core.campaign.product import Product
from .models import UserTable, CampaignTable, ProductTable, DonationTable, PurchaseTable, CampaignMediaTable, ProductMediaTable
from decimal import Decimal
from typing import List

class DjangoGetUser(GetModel[User]):
    def get(self, email: str) -> User:
        user_table = UserTable.objects.get(email=email)
        user = UserTable.to_user(user_table)
        return user
    
    def get_all(self) -> List[User]:
        user_tables = UserTable.objects.all()
        users = [UserTable.to_user(user_table) for user_table in user_tables]
        return users


class DjangoSaveUser(SaveModel[User]):
    def __init__(self) -> None:
        super().__init__(User)
        
    def save(self, user: User) -> None:
        user_table = UserTable.from_user(user)
        user_table.save()


class DjangoExistsUser(ExistsModel):
    def exists(self, user_id: str) -> bool:
        return UserTable.objects.filter(email=user_id).exists()


class DjangoGetCampaign(GetModel[Campaign]):
    def get(self, campaign_id: str) -> Campaign:
        campaign_table = CampaignTable.objects.get(id=campaign_id)
        campaign = CampaignTable.to_campaign(campaign_table)
        return campaign
    
    def get_all(self) -> List[Campaign]:
        campaign_tables = CampaignTable.objects.all() 
        campaigns = [CampaignTable.to_campaign(campaign_table) for campaign_table in campaign_tables]
        return campaigns


class DjangoSaveCampaign(SaveModel[Campaign]):
    def __init__(self) -> None:
        super().__init__(Campaign)
        
    def save(self, campaign: Campaign) -> None:
        campaign_table = CampaignTable.from_campaign(campaign)
        campaign_table.save()


class DjangoDeleteCampaign(DeleteModel[Campaign]):
    def delete(self, campaign_id: str) -> None:
        campaign_table = CampaignTable.objects.get(id=campaign_id)
        campaign_table.delete()


class DjangoGetProduct(GetModel[Product]):
    def get(self, product_id: str) -> Product:
        product_table = ProductTable.objects.get(id=product_id)
        product = ProductTable.to_product(product_table)
        return product
    
    def get_all(self) -> List[Product]:
        product_tables = ProductTable.objects.all()
        products = [ProductTable.to_product(product_table) for product_table in product_tables]
        return products


class DjangoSaveProduct(SaveModel[Product]):
    def __init__(self) -> None:
        super().__init__(Product)
        
    def save(self, product: Product) -> None:
        product_table = ProductTable.from_product(product)
        product_table.save()

class DjangoSaveDonation(EventSubscriber[DonateEvent]):
    def __init__(self) -> None:
        super().__init__(DonateEvent)
        
    def save(self, user_id: str, campaign_id: str, amount: Decimal) -> None:
        user_table = UserTable.objects.get(email=user_id)
        campaign_table = CampaignTable.objects.get(id=campaign_id)
        donation_table = DonationTable(user=user_table, campaign=campaign_table, amount=amount)
        donation_table.save()
    
    def handle(self, event: DonateEvent) -> None:
        user_id = event.user_id
        campaign_id = event.campaign_id
        amount = event.amount
        self.save(user_id, campaign_id, amount)


class DjangoSavePurchase(EventSubscriber[BuyEvent]):
    def __init__(self) -> None:
        super().__init__(BuyEvent)
        
    def save(self, user_id: str, product_id: str) -> None:
        user_table = UserTable.objects.get(email=user_id)
        product_table = ProductTable.objects.get(id=product_id)
        purchase_table = PurchaseTable(user=user_table, product=product_table, price=product_table.price)
        purchase_table.save()
    
    def handle(self, event: BuyEvent) -> None:
        user_id = event.user_id
        product_id = event.product_id
        self.save(user_id, product_id)


class DjangoSaveCampaignMedia(EventSubscriber[AddCampaignImageEvent]):
    def __init__(self) -> None:
        super().__init__(AddCampaignImageEvent)
        
    def save(self, campaign_id: str, image: str) -> None:
        campaign_table = CampaignTable.objects.get(id=campaign_id)
        campaign_media_table = CampaignMediaTable(campaign=campaign_table, media=image)
        campaign_media_table.save()
    
    def handle(self, event: AddCampaignImageEvent) -> None:
        campaign_id = event.campaign_id
        image = event.image
        self.save(campaign_id, image)


class DjangoSaveProductMedia(EventSubscriber[AddProductImageEvent]):
    def __init__(self) -> None:
        super().__init__(AddProductImageEvent)
        
    def save(self, product_id: str, image: str) -> None:
        product_table = ProductTable.objects.get(id=product_id)
        product_media_table = ProductMediaTable(product=product_table, media=image)
        product_media_table.save()
    
    def handle(self, event: AddProductImageEvent) -> None:
        product_id = event.product_id
        image = event.image
        self.save(product_id, image)


class DjangoDeleteCampaignMedia(EventSubscriber[DeleteCampaignImageEvent]):
    def __init__(self) -> None:
        super().__init__(DeleteCampaignImageEvent)
        
    def delete(self, campaign_id: str, image: str) -> None:
        campaign_table = CampaignTable.objects.get(id=campaign_id)
        campaign_media_table = CampaignMediaTable.objects.get(campaign=campaign_table, url=image)
        campaign_media_table.delete()
    
    def handle(self, event: DeleteCampaignImageEvent) -> None:
        campaign_id = event.campaign_id
        image = event.image
        self.delete(campaign_id, image)


class DjangoDeleteProductMedia(EventSubscriber[DeleteProductImageEvent]):
    def __init__(self) -> None:
        super().__init__(DeleteProductImageEvent)
        
    def delete(self, product_id: str, image: str) -> None:
        product_table = ProductTable.objects.get(id=product_id)
        product_media_table = ProductMediaTable.objects.get(product=product_table, url=image)
        product_media_table.delete()
    
    def handle(self, event: DeleteProductImageEvent) -> None:
        product_id = event.product_id
        image = event.image
        self.delete(product_id, image)

EventPublisher.subscribe(DjangoSaveUser())
EventPublisher.subscribe(DjangoSaveCampaign())
EventPublisher.subscribe(DjangoSaveProduct())
EventPublisher.subscribe(DjangoSaveDonation())
EventPublisher.subscribe(DjangoSavePurchase())
EventPublisher.subscribe(DjangoSaveCampaignMedia())
EventPublisher.subscribe(DjangoSaveProductMedia())
EventPublisher.subscribe(DjangoDeleteCampaignMedia())
EventPublisher.subscribe(DjangoDeleteProductMedia())