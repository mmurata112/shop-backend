from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserDetails(Base):
    __tablename__ = "user_details"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    full_name = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    phone = Column(String(50), nullable=True)

    # Relationships
    user = relationship("User", back_populates="details")
