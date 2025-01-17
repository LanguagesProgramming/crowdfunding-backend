from .campaign import Campaign
from .product import Product
from .dto import CreateCampaignDto, CampaignDto, CreateProductDto, ProductDto
from typing import Dict, Any

class ProductMapper:
    def to_product(self, data: Dict[str, Any]) -> Product:
        product: Product = Product.create(**data)
        return product

    def to_dto(self, product: Product) -> ProductDto:
        dto: ProductDto = ProductDto(product.id, product.name, product.price, product.discount, product.campaignId, product.images)
        return dto


class CampaignMapper:
    def to_campaign(self, dto: CreateCampaignDto) -> Campaign:
        campaign: Campaign = Campaign.create(dto.user_id, dto.title, dto.category, dto.description, ProductMapper().to_product(dto.product), dto.goal, dto.images)
        return campaign

    def to_dto(self, campaign: Campaign) -> CampaignDto:
        dto: CampaignDto = CampaignDto(campaign.id, campaign.userId, campaign.title, campaign.category, campaign.description, ProductMapper().to_dto(campaign.product), campaign.goal, campaign.current_money, campaign.images)
        return dto
