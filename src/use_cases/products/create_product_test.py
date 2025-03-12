import uuid

from src.repositories.in_memory.in_memory_products_repository import InMemoryProductsRepository
from src.use_cases.products.create_product import CreateProductUseCase


def test_it_should_be_possible_to_create_a_product() -> None:
    """."""
    product_repository = InMemoryProductsRepository()
    sut = CreateProductUseCase(product_repository)

    in_memory_products_list = product_repository.products

    product = {
        "id": uuid.uuid4(),
        "name": "Garrafa Térmica",
        "description": "Garrafa térmica portátil, mantém líquidos quentes ou frios.",
        "price": 129.90,
        "quantity": 1,
    }

    response = sut.execute(product)

    assert response.status_code == 201
    assert len(in_memory_products_list) == 1
    assert in_memory_products_list[0]["name"] == "Garrafa Térmica"
