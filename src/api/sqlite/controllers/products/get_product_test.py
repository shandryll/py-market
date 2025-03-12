import requests

from src.lib.sqlite import create_database, delete_database


def test_it_should_be_possible_to_find_a_product_by_name_in_sqlite() -> None:
    """."""
    delete_database("test.db")
    create_database("test.db")

    product = {
        "name": "Garrafa",
        "price": 87.90,
        "quantity": 1,
    }

    requests.post("http://localhost:3000/products", json=product)

    product_name = "Garrafa"
    response = requests.get(f"http://localhost:3000/products/{product_name}")

    assert response.status_code == 200
    assert response.body["name"] == "Garrafa"
