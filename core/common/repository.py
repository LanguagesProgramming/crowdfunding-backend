from .events import EventSubscriber, ModelCreatedEvent
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Type

Model = TypeVar('Model')

class GetModel(ABC, Generic[Model]):
    @abstractmethod
    def get_all(self) -> List[Model]: ...
    
    @abstractmethod
    def get(self, id: str) -> Model: ...


class SaveModel(EventSubscriber[ModelCreatedEvent[Model]], Generic[Model]):
    def __init__(self, modelType: Type[Model]) -> None:
        super().__init__(ModelCreatedEvent[modelType])
        
    @abstractmethod
    def save(self, model: Model): ...
    
    def handle(self, event: ModelCreatedEvent[Model]) -> None:
        self.save(event.get_model())


class ExistsModel(ABC):
    @abstractmethod
    def exists(self, id: str) -> bool: ...
   
    
class DeleteModel(ABC, Generic[Model]):
    @abstractmethod
    def delete(self, id: str) -> None: ...