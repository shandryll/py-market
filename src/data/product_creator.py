from src.models.redis.repository.interfaces.products_repository import (
    IProductsRepository as RedisProductRepository,
)
from src.models.sqlite.repository.interfaces.products_repository import (
    IProductsRepository as SQliteProductRepository,
)
from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse


class ProductCreator:
    def __init__(
        self,
        redis_repo: RedisProductRepository,
        sqlite_repo: SQliteProductRepository,
    ) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = sqlite_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        """."""
        body = http_request.body

        name = body.get("name")
        price = body.get("price")
        quantity = body.get("quantity")
        self.__insert_product_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)

        return self.__format_response()

    def __insert_product_in_sql(self, name: str, price: float, quantity: int) -> None:
        self.__sqlite_repo.create(name, price, quantity)

    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:
        product_key = name
        value = f"{price}, {quantity}"
        self.__redis_repo.insert_expiration(product_key, value, 60)

    def __format_response(self) -> HttpResponse:
        return HttpResponse(
            status_code=201,
            body={
                "type": "PRODUCT",
                "count": 1,
                "message": "Product registered successfully.",
            },
        )
