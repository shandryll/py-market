import requests


def test_it_should_be_able_to_create_a_product() -> None:
    """."""
    product = {
        "name": "Garrafa Térmica",
        "price": 129.90,
        "quantity": 1,
    }

    response = requests.post("http://localhost:3000/products", json=product)

    print(response)
