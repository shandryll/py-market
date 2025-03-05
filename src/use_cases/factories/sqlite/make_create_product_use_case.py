from src.lib.sqlite import SqliteConnectionHandler
from src.repositories.sqlite.sqlite_products_repository import SQliteProductsRepository
from src.use_cases.products.create_product import CreateProductUseCase

sqlite_connection_handle = SqliteConnectionHandler("test.db")


def make_create_product_use_case() -> None:
    """."""
    products_repository = SQliteProductsRepository(sqlite_connection_handle.connect())
    use_case = CreateProductUseCase(products_repository)

    return use_case
