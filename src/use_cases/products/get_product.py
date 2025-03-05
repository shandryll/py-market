from src.repositories.products_repository import IProductsRepository
from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse


class GetProductUseCase:
    def __init__(self, products_repository: IProductsRepository) -> None:
        self.__products_repository = products_repository

    def execute(self, request: HttpRequest) -> HttpResponse:
        """."""
        product_name = request.params
        product = self.__products_repository.find_by_name(product_name)

        if not product:
            return None

        return product
