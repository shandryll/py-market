from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse

from ..products_repository import IProductsRepository


class InMemoryProductsRepository(IProductsRepository):
    def __init__(self) -> None:
        self.products = []

    def create(self, data: HttpRequest) -> HttpResponse:
        """."""
        product = {
            "name": data["name"],
            "price": data["price"],
            "quantity": data["quantity"],
        }
        self.products.append(product)

        return HttpResponse(body=product, status_code=201)

    def find_by_name(self, params: HttpRequest) -> HttpResponse:
        """."""
        product_name = params["name"]
        product = next((item for item in self.products if item["name"] == product_name), None)

        if not product:
            return None

        return HttpResponse(body=product, status_code=200)
