from flask import Blueprint, jsonify, request

from src.api.sqlite.controllers.products.create import create_product
from src.schemas.http_request import HttpRequest
from src.schemas.http_response import HttpResponse

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def create() -> HttpResponse:
    """."""
    http_request = HttpRequest(body=request.json)
    http_response = create_product(http_request)
    return jsonify(http_response.body), http_response.status_code


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name: str) -> None:
    """."""
    return jsonify({"message": f"Produto cadastrado: {product_name}"}), 200
