from core.user.services import UserService
from core.campaign.services import CampaignService
from core.campaign.category import CampaignCategory
from core.user.dto import CreateUserDto, ChangeUserDto
from core.campaign.dto import CreateCampaignDto, ChangeCampaignDto, ChangeProductDto
from .repository import (DjangoGetUser, DjangoGetCampaign, DjangoExistsUser,
                         DjangoDeleteCampaign, DjangoGetProduct)
from .response import success_response, validate
from .serializer import (CreateUserSerializer, ChangeUserSerializer, CreateCampaignSerializer,
                         ChangeCampaignSerializer, DonationSerializer, ChangeProductSerializer,
                         BuyProductSerializer, CampaignMediaSerializer, ProductMediaSerializer)
from rest_framework.views import APIView
from rest_framework.request import Request
from dataclasses import asdict
from decimal import Decimal
from typing import Optional

user_service = UserService(
        get_user=DjangoGetUser(),
        exists_user=DjangoExistsUser(),
        get_campaign=DjangoGetCampaign()
    )

campaign_service = CampaignService(
    get_campaign=DjangoGetCampaign(),
    delete_campaign=DjangoDeleteCampaign(),
    get_product=DjangoGetProduct()
)

class UserApi(APIView):
    @validate()
    def get(self, request, user_id: Optional[str] = None, *args, **kwargs):
        if user_id is not None:
            user = user_service.find_user(user_id)
            data = asdict(user)
            for campaign in data['campaigns']:
                campaign['category'] = campaign['category'].name
            return success_response(data)
        users = user_service.get_all()
        datas = []
        for user in users:
            data = asdict(user)
            for campaign in data['campaigns']:
                campaign['category'] = campaign['category'].name
            datas.append(data)
        return success_response(datas)
        
    @validate(CreateUserSerializer)
    def post(self, request: Request):
        user = user_service.create_user(CreateUserDto(**request.data))
        return success_response(asdict(user))
    
    @validate(ChangeUserSerializer)
    def put(self, request: Request):
        user = user_service.change_user_data(ChangeUserDto(**request.data))
        data = asdict(user)
        for campaign in data['campaigns']:
            campaign['category'] = campaign['category'].name
        return success_response(data)


class CampaignApi(APIView):
    def get(self, request, name: Optional[str] = None, category: Optional[str] = None, *args, **kwargs):
        if category is not None:
            category = CampaignCategory(category)
        campaigns = campaign_service.filter_campaigns(name, category)
        datas = []
        for campaign in campaigns:
            data = asdict(campaign)
            data['category'] = campaign.category.name
            datas.append(data)
        return success_response(datas)
    
    @validate(CreateCampaignSerializer)
    def post(self, request: Request):
        request.data['category'] = CampaignCategory(request.data['category'])
        campaign = campaign_service.create_campaign(CreateCampaignDto(**request.data))
        data = asdict(campaign)
        data['category'] = campaign.category.name
        return success_response(data)
    
    @validate(ChangeCampaignSerializer)
    def put(self, request: Request):
        category = request.data.get('category')
        if category is not None:
            category = CampaignCategory(category)
        campaign = campaign_service.change_campaign_data(ChangeCampaignDto(
            campaign_id=request.data['campaign_id'],
            title=request.data.get('title'),
            category=category,
            description=request.data.get('description')
        ))
        data = asdict(campaign)
        data['category'] = campaign.category.name
        return success_response(data)
    
    @validate()
    def delete(self, campaign_id: str):
        campaign = campaign_service.delete_campaign(campaign_id)
        data = asdict(campaign)
        data['category'] = campaign.category.name
        return success_response(data)


class ProductApi(APIView):
    @validate(ChangeProductSerializer)  
    def put(self, request: Request):
        product = campaign_service.change_product_data(ChangeProductDto(**request.data))
        return success_response(asdict(product))


class DonationApi(APIView):
    @validate(DonationSerializer)
    def post(self, request: Request):
        data = request.data
        user = user_service.donate(data['user_id'], data['campaign_id'], Decimal(data['amount']))
        data = asdict(user)
        for campaign in data['campaigns']:
            campaign['category'] = campaign['category'].name
        return success_response(data)


class BuyApi(APIView):
    @validate()
    def get(self, request, user_id: str, *args, **kwargs):
        purchases = campaign_service.get_purchases(user_id)
        datas = [asdict(purchase) for purchase in purchases]
        return success_response(datas)
    
    @validate(BuyProductSerializer)
    def post(self, request: Request):
        data = request.data
        user = user_service.buy(data['user_id'], data['campaign_id'], int(data['stock']))
        data = asdict(user)
        for campaign in data['campaigns']:
            campaign['category'] = campaign['category'].name
        return success_response(data)



class CampaignMediaApi(APIView):
    @validate(CampaignMediaSerializer)
    def post(self, request: Request):
        campaign = campaign_service.add_campaign_image(request.data['campaign_id'], request.data['image'])
        return success_response(asdict(campaign))
    
    def delete(self, campaign_id: str, image: str):
        campaign = campaign_service.delete_campaign_image(campaign_id, image)
        return success_response(asdict(campaign))


class ProductMediaApi(APIView):
    @validate(ProductMediaSerializer)
    def post(self, request: Request):
        product = campaign_service.add_product_image(request.data['product_id'], request.data['image'])
        return success_response(asdict(product))
    
    def delete(self, product_id: str, image: str):
        product = campaign_service.delete_product_image(product_id, image)
        return success_response(asdict(product))
