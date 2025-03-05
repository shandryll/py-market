from typing import Union

from src.models.product import IProduct
from src.repositories.products_repository import IProductsRepository


class GetProductUseCase:
    def __init__(self, products_repository: IProductsRepository) -> None:
        self.__products_repository = products_repository

    def execute(self, data: IProduct) -> Union[dict, None]:
        """."""
        response = self.__products_repository.find_by_name(data)

        return response
