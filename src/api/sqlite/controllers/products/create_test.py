import requests

from src.lib.sqlite import create_database, delete_database


def test_it_should_be_possible_to_create_a_product() -> None:
    """."""
    delete_database("test.db")
    create_database("test.db")

    product = {
        "name": "Garrafa Térmica",
        "price": 87.90,
        "quantity": 1,
    }

    response = requests.post("http://localhost:3000/products", json=product)

    assert response.status_code == 201
