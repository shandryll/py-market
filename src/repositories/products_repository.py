from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union


@dataclass
class IProduct:
    name: str
    price: float
    quantity: int


class IProductsRepository(ABC):
    @abstractmethod
    def create(self, data: IProduct) -> dict:
        """."""
        pass

    @abstractmethod
    def find_by_name(self, data: IProduct) -> Union[dict, None]:
        """."""
        pass
