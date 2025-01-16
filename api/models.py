from core.campaign.category import CampaignCategory
from core.user.user import User
from core.campaign.campaign import Campaign
from core.campaign.product import Product
from django.db import models

class UserTable(models.Model):
    email = models.CharField(max_length=255, unique=True, primary_key=True)
    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'user'

    @classmethod
    def from_user(cls, user: User) -> 'UserTable':
        #TODO
        user_table : UserTable
        return user_table
    
    @classmethod
    def to_user(cls, user_table: 'UserTable') -> User:
        #TODO
        user : User
        return user


class CampaignTable(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=25, choices=[(category.name, category.value) for category in CampaignCategory])
    description = models.TextField()
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    current_money = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'campaign'

    @classmethod
    def from_campaign(cls, campaign: Campaign) -> 'CampaignTable':
        #TODO
        campaign_table : CampaignTable
        return campaign_table
    
    @classmethod
    def to_campaign(cls, campaign_table: 'CampaignTable') -> Campaign:
        #TODO
        campaign : Campaign
        return campaign
    

class ProductTable(models.Model):
    id = models.UUIDField(primary_key=True)
    campaign = models.ForeignKey(CampaignTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'product'

    @classmethod
    def from_product(cls, product: Product) -> 'ProductTable':
        #TODO
        product_table : ProductTable
        return product_table
    
    @classmethod
    def to_product(cls, product_table: 'ProductTable') -> Product:
        #TODO
        product : Product
        return product
    
    
class DonationTable(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    campaign = models.ForeignKey(CampaignTable, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'donation'
        constraints = [
            models.UniqueConstraint(fields=['user', 'campaign'], name='unique_donation')
        ]


class PurchaseTable(models.Model):
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = 'purchase'
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_purchase')
        ]
        

class CampaignMediaTable(models.Model):
    campaign = models.ForeignKey(CampaignTable, on_delete=models.CASCADE)
    media = models.TextField()
    
    class Meta:
        db_table = 'campaign_media'
        

class ProductMediaTable(models.Model):
    product = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    media = models.TextField()
    
    class Meta:
        db_table = 'product_media'
