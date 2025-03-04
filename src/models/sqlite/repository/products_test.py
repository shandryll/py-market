from src.db.sqlite import create_database, delete_database
from src.models.sqlite.settings.connection import SqliteConnectionHandler

from .products import ProductsRepository

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()


def test_insert_product() -> None:
    """."""
    delete_database("test.db")
    create_database("test.db")

    repo = ProductsRepository(conn)

    name = "any_name"
    price = 12.34
    quantity = 5

    repo.insert_product(name, price, quantity)


def test_find_product() -> None:
    """."""
    delete_database("test.db")
    create_database("test.db")

    repo = ProductsRepository(conn)

    name = "any_name"

    response = repo.find_product_by_name(name)

    assert type(response) is tuple
    assert response == (1, "any_name", 12.34, 5)
