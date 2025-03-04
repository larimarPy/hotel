from sqlalchemy import Column, Integer, ForeignKey
from bot.database import Base

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    menu_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    count = Column(Integer, default=1)

    