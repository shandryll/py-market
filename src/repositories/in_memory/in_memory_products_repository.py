from src.models.product import IProduct
from src.repositories.products_repository import IProductsRepository


class InMemoryProductsRepository(IProductsRepository):
    def __init__(self) -> None:
        self.products = []

    def find_by_name(self, name: str) -> tuple:
        """."""
        product = next((item for item in self.products if item.name == name), None)
        if not product:
            return None

        return product

    def create(self, product: IProduct) -> IProduct:
        """."""
        self.products.append(product)

        return product
