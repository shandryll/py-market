from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class IProduct:
    name: str
    price: float
    quantity: int


class IProductsRepository(ABC):
    @abstractmethod
    def find_by_name(self, name: str) -> tuple:
        """."""
        pass

    @abstractmethod
    def create(self, product: IProduct) -> dict:
        """."""
        pass
