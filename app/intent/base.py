from abc import ABC, abstractmethod

class IntentEngine(ABC):

    @abstractmethod
    def respond(self, message: str):
        pass
