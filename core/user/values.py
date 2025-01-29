from core.common.values import PatternMatcher, StringValue
from .exceptions import (InvalidUserNameException, InvalidUserEmailException, InvalidUserPasswordException,
                         InvalidPhoneNumberException)
import bcrypt

class UserName:
    __REGREX = "^(?=.{4,16}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, user_name: str) -> None:
        self.__value = StringValue(user_name)
        self.__validate()
    
    def __validate(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidUserNameException.invalid_name(self.get_value())
    
    def get_value(self) -> str:
        return self.__value.get_value()
    
    def __str__(self) -> str:
        return self.get_value()


class UserEmail:
    __REGREX = "^[a-zA-Z0-9._%+-]+@gmail\\.com$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, value: str) -> None:
        self.__value = StringValue(value)
        self.__validate()
        
    def __validate(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidUserEmailException.invalid_user_email(self.get_value())
    
    def get_value(self) -> str:
        return self.__value.get_value()
    
    def __str__(self) -> str:
        return self.get_value()


class UserPassword:
    __REGREX = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, password: str) -> None:
        self.__value = self.encode(password)
        self.__validate()
    
    def __validate(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidUserPasswordException.invalid_password(self.get_value())
    
    @classmethod
    def verify(cls, password: str, hashed: str) -> bool:
        password_bytes = password.encode()
        return bcrypt.checkpw(password_bytes, hashed.encode())
    
    @classmethod
    def encode(cls, password: str) -> str:
        password_bytes = password.encode()
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt(12))
        return hashed.decode()
    
    def get_value(self) -> str:
        return self.__value


class UserPhoneNumber:
    __REGREX = "^(0)?9\\d{8}$"
    __MATCHER = PatternMatcher(__REGREX)
    
    def __init__(self, value: str) -> None:
        self.__value = StringValue(value)
        self.__validate()
        
    def __validate(self) -> None:
        if not self.__MATCHER.match(self.get_value()):
            raise InvalidPhoneNumberException.invalid_phone_number(self.get_value())
    
    def get_value(self) -> str:
        return self.__value.get_value()