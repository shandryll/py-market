from flask import Blueprint, jsonify

products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def create() -> None:
    """."""
    return jsonify({"message": "Produto cadastrado"}), 200


@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name: str) -> None:
    """."""
    return jsonify({"message": f"Produto cadastrado: {product_name}"}), 200
