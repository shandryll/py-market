from sqlite3 import Connection as SqliteConnection

from repositories.products_repository import IProductsRepository
from schemas.http_request import HttpRequest
from schemas.http_response import HttpResponse


class SQliteProductsRepository(IProductsRepository):
    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn

    def create(self, data: HttpRequest) -> HttpResponse:
        """."""
        cursor = self.__conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
            (data["name"], data["price"], data["quantity"]),
        )
        self.__conn.commit()

        return HttpResponse(body=data, status_code=201)

    def find_by_name(self, name: str) -> tuple:
        """."""
        cursor = self.__conn.cursor()
        cursor.execute(
            "SELECT * FROM products WHERE name = ?",
            (name),
        )
        product = cursor.fetchone()
        return product
