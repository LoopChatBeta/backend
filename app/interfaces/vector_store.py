from abc import ABC, abstractmethod

class VectorStore(ABC):

    @abstractmethod
    def search(self, query: str):
        pass
