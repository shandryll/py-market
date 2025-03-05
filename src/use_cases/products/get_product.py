from src.repositories.products_repository import IProductsRepository
from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse


class GetProductUseCase:
    def __init__(self) -> None:
        self.__product_repository = IProductsRepository

    def execute(self, body: HttpRequest) -> HttpResponse:
        """."""
        product = self.__product_repository.find_by_name(body.name)

        print("---")
        print(product)
        print("---")

        if not product:
            raise Exception("Product not found.")

        return product
