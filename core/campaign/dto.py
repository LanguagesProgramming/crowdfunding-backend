from .category import CampaignCategory
from dataclasses import dataclass
from typing import List, Optional
from decimal import Decimal

@dataclass
class CreateProductDto:
    name: str
    price: Decimal
    discoint: Decimal
    images: List[str]
  
    
@dataclass
class ProductDto:
    product_id: str
    name: str
    price: Decimal
    discoint: Decimal
    images: List[str]
    
       
@dataclass
class CreateCampaignDto:
    user_id: str
    title: str
    category: CampaignCategory
    description: str
    product: CreateProductDto
    images: List[str]


@dataclass
class ChangeCampaignDto:
    campaign_id: str
    title: Optional[str]
    category: Optional[CampaignCategory]
    description: Optional[str]


@dataclass
class CampaignDto:
    campaign_id: str
    user_id: str
    title: str
    category: CampaignCategory
    description: str
    product: ProductDto
    images: List[str]


@dataclass
class ChangeProductDto:
    product_id: str
    name: Optional[str]
    price: Optional[Decimal]
    discoint: Optional[Decimal]