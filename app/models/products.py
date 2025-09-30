from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0, nullable=False)

    # Relationships
    order_items = relationship("OrderItem", back_populates="product")