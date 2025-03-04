from sqlalchemy import Column, String, Integer, Boolean
from bot.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    