from .values import PatternMatcher, ID
from .exception import InvalidBase64FormatException, MediaNotFoundException
import base64
import os

class Base64SaveStorageImage:
    __URL_REGEX = r'^data:image\/(png|jpeg|jpg|gif|bmp|webp);base64,[A-Za-z0-9+/]+={0,2}$'
    __MATCHER = PatternMatcher(__URL_REGEX)
    BASE = "resources/media"
    
    def __init__(self, folder_name: str) -> None:
        self.__folder_name = folder_name
        
    def save(self, image: str) -> str:
        self.verify_base64(image)
        binary_image = base64.b64decode(image.split(",")[1])
        image_url = f'{self.BASE}/{self.__folder_name}/{ID.generate()}.png'
        with open(image_url, "wb") as file:
            file.write(binary_image)
        return image_url
    
    @classmethod
    def verify_base64(cls, image: str) -> None:
        if not cls.__MATCHER.match(image):
            raise InvalidBase64FormatException.invalid_format()


class DeleteStorageImage:
    def delete(self, path_name: str) -> str:
        if not path_name.startswith(Base64SaveStorageImage.BASE):
            path_name = Base64SaveStorageImage.BASE + '/' + path_name
        if os.path.exists(path_name):
            os.remove(path_name)
            return path_name
        raise MediaNotFoundException.media_not_found(path_name)