from typing import Union

from src.repositories.products_repository import IProductsRepository


class GetProductUseCase:
    def __init__(self, products_repository: IProductsRepository) -> None:
        self.__products_repository = products_repository

    def execute(self, name: str) -> Union[dict, None]:
        """."""
        response = self.__products_repository.find_by_name(name)

        return response
