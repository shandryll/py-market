from typing import Union

from src.repositories.products_repository import IProductsRepository


class GetProductUseCase:
    def __init__(self, products_repository: IProductsRepository) -> None:
        self.__products_repository = products_repository

    def execute(self, product_name: str) -> Union[dict, None]:
        """."""
        response = self.__products_repository.find_by_name(product_name)

        return response
