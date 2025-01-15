from .user import User
from .dto import CreateUserDto, UserDto

class UserMapper:
    def to_user(self, dto: CreateUserDto) -> User:
        #TODO
        user : User
        return user
    
    def to_dto(self, user: User) -> UserDto:
        #TODO
        dto : UserDto
        return dto