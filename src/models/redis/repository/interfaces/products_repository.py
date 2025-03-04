from abc import abstractmethod
from typing import Union


class IProductsRepository:
    @abstractmethod
    def insert(self, key: str, value: str) -> None:
        """."""
        pass

    @abstractmethod
    def get_key(self, key: str) -> Union[str, None]:
        """."""
        pass

    @abstractmethod
    def insert_expiration(self, key: str, value: str, expiration: int) -> None:
        """."""
        pass

    @abstractmethod
    def insert_hash(self, key: str, field: str, value: str) -> None:
        """."""
        pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> Union[str, None]:
        """."""
        pass

    @abstractmethod
    def insert_hash_expiration(self, key: str, field: str, value: str, expiration: int) -> None:
        """."""
        pass
