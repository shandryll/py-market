import pytest

from src.repositories.in_memory.in_memory_products_repository import InMemoryProductsRepository
from src.use_cases.products.get_product import GetProductUseCase


@pytest.mark.skip(reason="Ignorando este teste por enquanto")
def test_get_product() -> None:
    """."""
    product_repository = InMemoryProductsRepository()
    sut = GetProductUseCase()

    product_name = {"name": "Garrafa Térmica"}
    teste = product_repository.find_by_name(product_name)

    # product = sut.execute(product_name)

    print("---")
    print(teste)
    print("---")

    assert teste == "teste"
