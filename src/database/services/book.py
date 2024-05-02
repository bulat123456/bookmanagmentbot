import logging
from typing import Optional, Sequence

from src.database.models import Book
from src.database.repositories import BookRepository

logger = logging.getLogger(__name__)


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    async def get_by_id(self, book_id: int) -> Optional[Book]:
        return await self.repository.get_by_id(book_id)

    async def get_by_genre(self, genre: str) -> Optional[Sequence[Book]]:
        return await self.repository.get_by_genre(genre)

    async def get_by_query(self, query: str) -> Optional[Sequence[Book]]:
        return await self.repository.get_by_query(query)

    async def get_all(self) -> Sequence[Book]:
        return await self.repository.get_all()

    async def create(self, title: str, author: str, description: str, genre: str) -> Book:
        result = await self.repository.create(title=title, author=author, description=description, genre=genre)
        await self.repository.commit()
        logger.info(f'New record in table {Book.__tablename__} with book_id={result.id}')
        return result

    async def get_genres(self):
        return await self.repository.get_genres()

    async def update(self, book: Book) -> None:
        await self.repository.update(book)
        await self.repository.commit()
