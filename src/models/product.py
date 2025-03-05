from dataclasses import dataclass


@dataclass
class IProduct:
    name: str
    price: float
    quantity: int
