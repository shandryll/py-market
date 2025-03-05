from src.repositories.in_memory.in_memory_products_repository import InMemoryProductsRepository
from src.use_cases.products.create_product import CreateProductUseCase


def test_create_product() -> None:
    """."""
    product_repository = InMemoryProductsRepository()
    sut = CreateProductUseCase(product_repository)

    in_memory_products_list = product_repository.products

    product = {
        "name": "Garrafa Térmica",
        "price": 129.90,
        "quantity": 1,
    }

    sut.execute(product)

    product = {
        "name": "Batom",
        "price": 31.20,
        "quantity": 2,
    }

    sut.execute(product)

    assert len(in_memory_products_list) == 2
    assert in_memory_products_list[0]["name"] == "Garrafa Térmica"
    assert in_memory_products_list[1]["name"] == "Batom"
