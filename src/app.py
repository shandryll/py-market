from flask import Flask

from api.controllers.products.routes import products_routes_bp
from models.redis.settings.connection import RedisConnectionHandler
from models.sqlite.settings.connection import SqliteConnectionHandler

redis_connection_handle = RedisConnectionHandler()
sqlite_connection_handle = SqliteConnectionHandler()

redis_connection_handle.connect()
sqlite_connection_handle.connect()


app = Flask(__name__)

app.register_blueprint(products_routes_bp)
