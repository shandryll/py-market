from src.lib.sqlite import SqliteConnectionHandler
from src.repositories.sqlite.sqlite_products_repository import SQliteProductsRepository
from src.use_cases.products.get_product import GetProductUseCase

sqlite_connection_handle = SqliteConnectionHandler("test.db")


def make_get_product_use_case() -> None:
    """."""
    products_repository = SQliteProductsRepository(sqlite_connection_handle.connect())
    use_case = GetProductUseCase(products_repository)

    return use_case
