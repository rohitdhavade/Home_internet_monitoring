from abc import ABC, abstractmethod

class SubscriberInterface(ABC):
    @abstractmethod
    def update():
        raise NotImplementedError

