from src.models.product import IProduct
from src.repositories.products_repository import IProductsRepository


class CreateProductUseCase:
    def __init__(self, products_repository: IProductsRepository) -> None:
        self.__products_repository = products_repository

    def execute(self, data: IProduct) -> dict:
        """."""
        response = self.__products_repository.create(data.body)

        return response
