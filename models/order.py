from sqlalchemy import Column, Integer, String, ForeignKey
from bot.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    items = Column(String, nullable=False)
    status = Column(String, default="В обработке")
