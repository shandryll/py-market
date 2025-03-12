from abc import ABC, abstractmethod
from typing import Union

from src.models.product import IProduct


class IProductsRepository(ABC):
    @abstractmethod
    def create(self, data: IProduct) -> dict:
        """."""
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> Union[dict, None]:
        """."""
        pass
