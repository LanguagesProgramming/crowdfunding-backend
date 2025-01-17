from typing import Optional
from core.common.events import EventPublisher
from core.common.repository import DeleteModel, GetModel
from .campaign import Campaign
from .product import Product
from .category import CampaignCategory
from .dto import CreateCampaignDto, CampaignDto, ChangeCampaignDto, ProductDto, ChangeProductDto
from .mapper import CampaignMapper, ProductMapper

class CampaignService:
    def __init__(self, get_campaign: GetModel[Campaign], delete_campaign: DeleteModel[Campaign],
                 get_product: GetModel[Product]) -> None:
        self.__mapper = CampaignMapper()
        self.__product_mapper = ProductMapper()
        self.__get_product = get_product
        self.__get_campaign = get_campaign
        self.__delete_campaign = delete_campaign
        
    def create_campaign(self, dto: CreateCampaignDto) -> CampaignDto:
        campaign = self.__mapper.to_campaign(dto)
        EventPublisher.publish()
        return self.__mapper.to_dto(campaign)
    
    def delete_campaign(self, campaign_id: str) -> CampaignDto:
        campaign = self.__get_campaign.get(campaign_id)
        self.__delete_campaign.delete(campaign_id)
        return self.__mapper.to_dto(campaign)

    def filter_campaigns(self, title: Optional[str], category: Optional[CampaignCategory]) -> list[CampaignDto]:
        campaigns = self.__get_campaign.get_all() 
        print(title, type(category), "AAAAAAAAAA")
        if category != None:
            campaigns = [campaign for campaign in campaigns if campaign.is_same_category(category)]

        if title != None:
            campaigns = [campaign for campaign in campaigns if campaign.matches_title(title)]

        return [self.__mapper.to_dto(campaign) for campaign in campaigns]
    
    def change_campaign_data(self, dto: ChangeCampaignDto) -> CampaignDto:
        campaign = self.__get_campaign.get(dto.campaign_id)
        campaign.change_data(dto.title, dto.category, dto.description)
        EventPublisher.publish()
        return self.__mapper.to_dto(campaign)
    
    def change_product_data(self, dto: ChangeProductDto) -> ProductDto:
        product = self.__get_product.get(dto.product_id)
        product.change_data(dto.name, dto.price, dto.discount)
        EventPublisher.publish()
        return self.__product_mapper.to_dto(product)
    
    def add_campaign_image(self, campaign_id: str, image: str) -> CampaignDto:
        campaign = self.__get_campaign.get(campaign_id)
        campaign.add_image(image)
        EventPublisher.publish()
        return self.__mapper.to_dto(campaign)
    
    def delete_campaign_image(self, campaign_id: str, image: str) -> CampaignDto:
        campaign = self.__get_campaign.get(campaign_id)
        campaign.delete_image(image)
        EventPublisher.publish()
        return self.__mapper.to_dto(campaign)
    
    def add_product_image(self, product_id: str, image: str) -> ProductDto:
        product = self.__get_product.get(product_id)
        product.add_image(image)
        EventPublisher.publish()
        return self.__product_mapper.to_dto(product)
    
    def delete_product_image(self, product_id: str, image: str) -> ProductDto:
        product = self.__get_product.get(product_id)
        product.delete_image(image)
        EventPublisher.publish()
        return self.__product_mapper.to_dto(product)
