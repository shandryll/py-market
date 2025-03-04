from src.models.sqlite.repository.interfaces.products_repository import IProductsRepository


class ProductFinder:
    def __init__(self, redis_repo: , sqlite_repo: IProductsRepository) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = sqlite_repo
