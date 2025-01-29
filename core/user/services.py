from core.common.events import EventPublisher
from core.common.repository import GetModel, ExistsModel
from core.campaign.campaign import Campaign
from .user import User
from .exceptions import UserIsAlreadyRegisteredException
from .dto import CreateUserDto, ChangeUserDto, UserDto
from .mapper import UserMapper
from decimal import Decimal
from typing import List

class UserService:
    def __init__(self, get_user: GetModel[User], exists_user: ExistsModel,
                 get_campaign: GetModel[Campaign]) -> None:
        self.__mapper = UserMapper()
        self.__get_user = get_user
        self.__exists_user = exists_user
        self.__get_campaign = get_campaign
    
    def create_user(self, dto: CreateUserDto) -> UserDto:
        if self.__exists_user.exists(dto.email):
            raise UserIsAlreadyRegisteredException.is_already_registered(dto.email)
        user = self.__mapper.to_user(dto)
        EventPublisher.publish()
        print(self.__mapper.to_dto(user))
        return self.__mapper.to_dto(user)
    
    def find_user(self, user_id: str) -> UserDto:
        user = self.__get_user.get(user_id)
        return self.__mapper.to_dto(user)
    
    def get_all(self) -> List[UserDto]:
        users = self.__get_user.get_all()
        return [self.__mapper.to_dto(user) for user in users]
    
    def change_user_data(self, dto: ChangeUserDto) -> UserDto:
        if dto.email is not None and self.__exists_user.exists(dto.email):
            raise UserIsAlreadyRegisteredException.is_already_registered(dto.email)
        user = self.__get_user.get(dto.user_id)
        user.change_data(dto.email, dto.name, dto.password, dto.phone_number)
        EventPublisher.publish()
        return self.__mapper.to_dto(user)
    
    def donate(self, user_id: str, campaign_id: str, amount: Decimal) -> UserDto:
        user = self.__get_user.get(user_id)
        campaign = self.__get_campaign.get(campaign_id)
        user.donate(campaign, amount)
        EventPublisher.publish()
        return self.__mapper.to_dto(user)
    
    def buy(self, user_id: str, campaign_id: str, stock: int) -> UserDto:
        user = self.__get_user.get(user_id)
        campaign = self.__get_campaign.get(campaign_id)
        user.buy(campaign, stock)
        EventPublisher.publish()
        return self.__mapper.to_dto(user)