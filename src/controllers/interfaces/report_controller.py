from abc import ABC, abstractmethod

class CustomerGenerateReportControlerInterface(ABC):

    @abstractmethod
    def generate_report(self, customer_id: int) -> dict:
        pass
