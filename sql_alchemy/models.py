import uuid

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String(80), nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
