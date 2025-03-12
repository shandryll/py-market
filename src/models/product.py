from typing import Optional

from pydantic import BaseModel


class IProduct(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool
    quantity: Optional[int] = 0
