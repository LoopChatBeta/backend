from abc import ABC, abstractmethod

class ConvoStore(ABC):

    @abstractmethod
    def save_message(
        self,
        conversation_id,
        role,
        content
    ):
        pass
