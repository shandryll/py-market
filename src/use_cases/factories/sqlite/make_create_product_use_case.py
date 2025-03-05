from repositories.sqlite.sqlite_products_repository import SQliteProductsRepository
from use_cases.products.create_product import CreateProductUseCase


def make_create_product_use_case() -> None:
    """."""
    products_repository = SQliteProductsRepository()
    use_case = CreateProductUseCase(products_repository)

    return use_case
