import requests


def test_it_should_be_able_to_create_a_product() -> None:
    """."""
    product = {
        "name": "Garrafa Térmica",
        "price": 87.90,
        "quantity": 1,
    }

    response = requests.post("http://localhost:3000/products", json=product)

    assert response.status_code == 201
