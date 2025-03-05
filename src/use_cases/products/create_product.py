from src.repositories.products_repository import IProductsRepository
from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse


class CreateProductUseCase:
    def __init__(self, products_repository: IProductsRepository) -> None:
        self.__products_repository = products_repository

    def execute(self, request: HttpRequest) -> HttpResponse:
        """."""
        response = self.__products_repository.create(request.body)

        return response
