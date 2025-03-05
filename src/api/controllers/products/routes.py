from flask import Blueprint, jsonify, request

from api.controllers.products.create import create_product
from schemas.http_request import HttpRequest
from schemas.http_response import HttpResponse

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def create() -> None:
    """."""
    http_request = HttpRequest(body=request.json)
    product = create_product(http_request)
    http_response = HttpResponse(product)
    return jsonify(http_response.body), http_response.status_code


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name: str) -> None:
    """."""
    return jsonify({"message": f"Produto cadastrado: {product_name}"}), 200
