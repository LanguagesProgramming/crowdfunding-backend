from .exception import InvalidIdException
import uuid
import re

class ID:
    def __init__(self, value: str) -> None:
        self.__value = StringValue(value)
        self.__validate()
    
    def __validate(self) -> None:
        try:
            uuid.UUID(self.__value.get_value())
        except:
            raise InvalidIdException.invalid_id(self.__value.get_value())
    
    def get_value(self) -> str:
        return self.__value.get_value()
    
    @staticmethod
    def generate() -> str:
        return str(uuid.uuid4())


class PatternMatcher:
    def __init__(self, pattern: str) -> None:
        self.__pattern = pattern
        
    def match(self, value: str) -> bool:
        return bool(re.match(self.__pattern, value))
 
    
class StringValue:
    def __init__(self, value: str, lower: bool = True) -> None:
        self.__lower = lower
        self.__value = self.__fix(value)
    
    def __fix(self, value: str) -> str:
        value = value.strip()
        if self.__lower: 
            return value.lower()
        return value
    
    def get_value(self) -> str:
        return self.__value