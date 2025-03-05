from src.repositories.in_memory.in_memory_products_repository import InMemoryProductsRepository
from src.schemas.http_request import HttpRequest
from src.use_cases.products.get_product import GetProductUseCase


def test_should_be_possible_to_find_a_product_by_name() -> None:
    """."""
    product_repository = InMemoryProductsRepository()
    sut = GetProductUseCase(product_repository)

    product = {
        "name": "Garrafa Térmica",
        "price": 129.90,
        "quantity": 1,
    }

    product_repository.create(product)

    http_request = HttpRequest(params={"name": "Garrafa Térmica"})

    product = sut.execute(http_request)

    assert product["name"] == "Garrafa Térmica"
