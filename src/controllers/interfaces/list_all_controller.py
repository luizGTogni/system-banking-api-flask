from abc import ABC, abstractmethod

class CustomerListAllControllerInterface(ABC):

    @abstractmethod
    def list_all(self) -> dict:
        pass
