from core.campaign.category import CampaignCategory
from rest_framework import serializers

class CreateUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    name = serializers.CharField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
    

class ChangeUserSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    email = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    
    
class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    discount = serializers.DecimalField(max_digits=10, decimal_places=2)
    images = serializers.ListField(child=serializers.CharField())
    
    
class CreateCampaignSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    title = serializers.CharField()
    category = serializers.ChoiceField(choices=[(category.name, category.value) for category in CampaignCategory])
    description = serializers.CharField()
    product = CreateProductSerializer()
    goal = serializers.DecimalField(max_digits=10, decimal_places=2)
    images = serializers.ListField(child=serializers.CharField())
    
    
class ChangeCampaignSerializer(serializers.Serializer):
    campaign_id = serializers.UUIDField()
    title = serializers.CharField(required=False)
    category = serializers.ChoiceField(choices=[(category.name, category.value) for category in CampaignCategory], required=False)
    description = serializers.CharField(required=False)


class ChangeProductSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    name = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    discoint = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    
    
class DonationSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    campaign_id = serializers.UUIDField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    

class BuyProductSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    campaign_id = serializers.UUIDField()
    stock = serializers.IntegerField()
    

class CampaignMediaSerializer(serializers.Serializer):
    campaign_id = serializers.UUIDField()
    image = serializers.CharField()
    

class ProductMediaSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    image = serializers.CharField()