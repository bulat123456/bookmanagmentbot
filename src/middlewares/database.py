from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import Update
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.database import (
    BookService
)
from src.database.repositories import (
    BookRepository
)


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_maker: async_sessionmaker):
        self.session_maker = session_maker

    async def __call__(
            self,
            handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
            update: Update,
            data: dict[str, Any],
    ):
        async with self.session_maker() as session:
            data['book_service'] = BookService(
                repository=BookRepository(session=session),
            )
            return await handler(update, data)
