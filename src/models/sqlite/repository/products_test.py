import pytest

from src.models.sqlite.settings.connection import SqliteConnectionHandler

from .products import ProductsRepository

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_product() -> None:
    """."""
    repo = ProductsRepository(conn)

    name = "any_name"
    price = 12.34
    quantity = 5

    repo.insert_product(name, price, quantity)


@pytest.mark.skip(reason="interacao com o banco de dados")
def test_find_product() -> None:
    """."""
    repo = ProductsRepository(conn)

    name = "any_name"

    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))
