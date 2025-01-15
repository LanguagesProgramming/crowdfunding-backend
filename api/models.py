from core.common.repository import GetModel, SaveModel, ExistsModel
from core.user.user import User
from core.campaign.campaign import Campaign
from core.campaign.product import Product
from django.db import models

class UserTable(models.Model):
    #TODO
    class Meta:
        db_table = 'user'

    @classmethod
    def to_user(cls, user: User) -> 'UserTable':
        #TODO
        user_table : UserTable
        return user_table
    
    @classmethod
    def from_user(cls, user_table: 'UserTable') -> User:
        #TODO
        user : User
        return user


class CampaignTable(models.Model):
    #TODO
    class Meta:
        db_table = 'campaign'

    @classmethod
    def to_campaign(cls, campaign: Campaign) -> 'CampaignTable':
        #TODO
        campaign_table : CampaignTable
        return campaign_table
    
    @classmethod
    def from_campaign(cls, campaign_table: 'CampaignTable') -> Campaign:
        #TODO
        campaign : Campaign
        return campaign
    

class ProductTable(models.Model):
    #TODO
    class Meta:
        db_table = 'product'

    @classmethod
    def to_product(cls, product: Product) -> 'ProductTable':
        #TODO
        product_table : ProductTable
        return product_table
    
    @classmethod
    def from_product(cls, product_table: 'ProductTable') -> Product:
        #TODO
        product : Product
        return product
    
    
class DonationTable(models.Model):
    #TODO
    class Meta:
        db_table = 'donation'


class PurchaseTable(models.Model):
    #TODO
    class Meta:
        db_table = 'purchase'
        

class CampaignMediaTable(models.Model):
    #TODO
    class Meta:
        db_table = 'campaign_media'
        

class ProductMediaTable(models.Model):
    #TODO
    class Meta:
        db_table = 'product_media'