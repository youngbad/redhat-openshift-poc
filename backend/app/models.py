from sqlalchemy import Boolean, Column, Integer, String

from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
