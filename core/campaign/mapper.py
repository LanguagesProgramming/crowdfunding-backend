from .campaign import Campaign
from .product import Product
from .dto import CreateCampaignDto, CampaignDto, CreateProductDto, ProductDto

class ProductMapper:
    def to_product(self, dto: CreateProductDto) -> Product:
        #TODO
        product : Product
        return product

    def to_dto(self, product: Product) -> ProductDto:
        #TODO
        dto : ProductDto
        return dto


class CampaignMapper:
    def to_campaign(self, dto: CreateCampaignDto) -> Campaign:
        #TODO
        campaign : Campaign
        return campaign

    def to_dto(self, campaign: Campaign) -> CampaignDto:
        #TODO
        dto : CampaignDto
        return dto