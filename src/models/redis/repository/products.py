from typing import Union

from redis import Redis

from .interfaces.products_repository import IProductsRepository


class RedisRepository(IProductsRepository):
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: str) -> None:
        """."""
        self.__redis_conn.set(key, value)

    def get_key(self, key: str) -> Union[str, None]:
        """."""
        value = self.__redis_conn.get(key)
        if value:
            return value.decode("utf-8")
        return None

    def insert_hash(self, key: str, field: str, value: str) -> None:
        """."""
        self.__redis_conn.hset(key, field, value)

    def get_hash(self, key: str, field: str) -> Union[str, None]:
        """."""
        value = self.__redis_conn.hget(key, field)
        if value:
            return value.decode("utf-8")
        return None

    def insert_expiration(self, key: str, value: str, expiration: int) -> None:
        """."""
        self.__redis_conn.set(key, value, ex=expiration)

    def insert_hash_expiration(self, key: str, field: str, value: str, expiration: int) -> None:
        """."""
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, expiration)
