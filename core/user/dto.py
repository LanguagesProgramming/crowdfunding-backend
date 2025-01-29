from core.campaign.dto import CampaignDto
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class CreateUserDto:
    email: str
    name: str
    password: str
    phone_number: str


@dataclass
class ChangeUserDto:
    user_id: str
    email: Optional[str]
    name: Optional[str]
    password: Optional[str]
    phone_number: Optional[str]


@dataclass
class UserDto:
    email: str
    name: str
    phone_number: str
    campaigns: List[CampaignDto]