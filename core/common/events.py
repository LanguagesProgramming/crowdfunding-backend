from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type, List
from typing import get_args

E = TypeVar('E', bound='Event')
Model = TypeVar('Model')

class Event(ABC): ...
   
    
class EventSubscriber(Generic[E], ABC):
    def __init__(self, event_type: Type[E]) -> None:
        self.__event_type = event_type
        
    @abstractmethod
    def handle(self, event: E) -> None: ...

    def supports(self, event: E) -> bool:
        if len(get_args(self.__event_type)) > 0 and isinstance(event, ModelCreatedEvent):
            return get_args(self.__event_type)[0] == type(event.get_model())
        else:
            return self.__event_type == type(event)


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
    
    def get_model(self) -> Model:
        return self.__created_model