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
        user_table = UserTable(
            email=user.email,
            phone=user.phone_number,
            name=user.name,
            password=user.password
        )
        return user_table
    
    @classmethod
    def to_user(cls, user_table: 'UserTable') -> User:
        user = User.load(
            user_id=user_table.email,
            email=user_table.email,
            name=user_table.name,
            password=user_table.password,
            phone_number=user_table.phone,
            campaigns=CampaignTable.objects.filter(user=user_table)
        )
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
        campaign_table = CampaignTable(
            id=campaign.id,
            user = UserTable.objects.get(email=campaign.userId),
            title = campaign.title,
            category = campaign.category.name,
            description = campaign.description,
            goal = campaign.goal,
            current_money = campaign.current_money
        )
        return campaign_table
    
    @classmethod
    def to_campaign(cls, campaign_table: 'CampaignTable') -> Campaign:
        campaign = Campaign.load(
            id = str(campaign_table.id),
            userId = campaign_table.user.email,
            title = campaign_table.title,
            category = CampaignCategory(campaign_table.category),
            description = campaign_table.description,
            goal = campaign_table.goal,
            current_money = campaign_table.current_money,
            images = [media_table.media for media_table in CampaignMediaTable.objects.filter(campaign=campaign_table)],
            product = ProductTable.to_product(ProductTable.objects.get(campaign=campaign_table))
        )
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
        product_table = ProductTable(
            id=product.id,
            campaign=CampaignTable.objects.get(id=product.campaignId),
            name=product.name,
            price=product.price,
            discount=product.discount
        )
        return product_table
    
    @classmethod
    def to_product(cls, product_table: 'ProductTable') -> Product:
        product = Product.load(
            id=str(product_table.id),
            name=product_table.name,
            price=product_table.price,
            discount=product_table.discount,
            campaignId=str(product_table.campaign.id),
            images=[media_table.media for media_table in ProductMediaTable.objects.filter(product=product_table)]
        )
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
