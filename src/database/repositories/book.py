from typing import Optional, Sequence

from sqlalchemy import insert, select, or_, func

from src.database.models import Book
from .base import BaseRepository


class BookRepository(BaseRepository):
    async def get_by_id(self, book_id: int) -> Optional[Book]:
        query = select(Book).where(Book.id == book_id)
        result = await self.session.scalar(query)
        return result

    async def get_by_genre(self, genre: str) -> Optional[Sequence[Book]]:
        query = select(Book).filter(Book.genre.ilike(f'%{genre}%'))
        result = await self.session.scalars(query)
        return result.all()

    async def get_genres(self) -> Sequence[Book]:
        query = select(Book).where(Book.is_delete == False).distinct(Book.genre).group_by(Book.genre)
        result = await self.session.scalars(query)
        return result.all()

    async def get_by_query(self, query: str) -> Optional[Sequence[Book]]:
        query = select(Book).filter(or_(Book.title.ilike(f'%{query}%'), Book.author.ilike(f'%{query}%')))
        result = await self.session.scalars(query)
        return result.all()

    async def get_all(self) -> Sequence[Book]:
        query = select(Book).where(Book.is_delete == False)
        result = await self.session.scalars(query)
        return result.all()

    async def create(self, **values) -> Book:
        query = insert(Book).values(values).returning(Book)
        result = await self.session.scalar(query)
        await self.session.flush()
        return result

    async def update(self, book: Book) -> None:
        await self.session.merge(book)
        await self.session.flush()
