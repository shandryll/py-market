from src.models.product import IProduct
from src.repositories.products_repository import IProductsRepository


class InMemoryProductsRepository(IProductsRepository):
    def __init__(self) -> None:
        self.products = []

    def find_by_name(self, params: IProduct) -> tuple:
        """."""
        product_name = params["name"]
        product = next((item for item in self.products if item["name"] == product_name), None)

        if not product:
            return None

        return product

    def create(self, data: IProduct) -> IProduct:
        """."""
        product = {
            "name": data["name"],
            "price": data["price"],
            "quantity": data["quantity"],
        }
        self.products.append(product)

        return product
