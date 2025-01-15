from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, List

E = TypeVar('E', bound='Event')
Model = TypeVar('Model')

class Event(ABC): ...
   
    
class EventSubscriber(Generic[E], ABC):
    def __init__(self, event_type: Type[E]) -> None:
        self.__event_type = event_type
        
    @abstractmethod
    def handle(self, event: E) -> None: ...

    def supports(self, event: E) -> bool:
        return isinstance(event, self.__event_type)


class EventPublisher:
    subscribers : List[EventSubscriber]= []
    events : List[Event] = []
    
    @classmethod
    def subscribe(cls, subscriber: EventSubscriber) -> None:
        cls.subscribers.append(subscriber)
    
    @classmethod  
    def publish(cls) -> None:
        for event in cls.events:
            for subscriber in cls.subscribers:
                if subscriber.supports(event):
                    subscriber.handle(event)
    
    @classmethod
    def add_event(cls, event: Event) -> None:
        cls.events.append(event)


class ModelCreatedEvent(Event, Generic[Model]):
    def __init__(self, created_model: Model) -> None:
        self.__created_model = created_model
    
    def get_created_model(self) -> Model:
        return self.__created_model


class ModelModifiedEvent(Event, Generic[Model]):
    def __init__(self, modified_model: Model) -> None:
        self.__modified_model = modified_model
    
    def get_modified_model(self) -> Model:
        return self.__modified_model