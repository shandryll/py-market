from flask import Flask

from src.api.sqlite.controllers.products.routes import products_routes_bp

app = Flask(__name__)

app.register_blueprint(products_routes_bp)
