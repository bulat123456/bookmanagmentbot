from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = Column(String)
    author: Mapped[str] = Column(String)
    description = Column(String)
    genre: Mapped[str] = Column(String)
    is_delete = Column(Boolean, default=False)
