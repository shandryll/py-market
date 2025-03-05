from sqlite3 import Connection as SqliteConnection

from models.product import IProduct
from repositories.products_repository import IProductsRepository


class SQliteProductsRepository(IProductsRepository):
    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn

    def find_by_name(self, name: str) -> tuple:
        """."""
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (name),
        )
        product = cursor.fetchone()
        return product

    def create(self, product: IProduct) -> None:
        """."""
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
            (product["name"], product["price"], product["quantity"]),
        )
        self.__conn.commit()
