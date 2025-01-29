from core.campaign.mapper import CampaignMapper
from .user import User
from .dto import CreateUserDto, UserDto

class UserMapper:
    def to_user(self, dto: CreateUserDto) -> User:
        user : User = User.create(dto.email, dto.name, dto.password, dto.phone_number)
        return user
    
    def to_dto(self, user: User) -> UserDto:
        dto : UserDto = UserDto(user.email, user.name, user.phone_number, [CampaignMapper().to_dto(campaign) for campaign in user.campaigns])
        return dto
